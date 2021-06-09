import sqlalchemy
import pytest
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from mysql.models import Base, TestUsers


class MysqlClient:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = 'mysql'
        self.port = 3306

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine,
                                    autocommit=False,
                                    autoflush=False,
                                    expire_on_commit=False 
                                    )()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def recreate_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()

    def create_table(self, key):
        if not inspect(self.engine).has_table(key):
            Base.metadata.tables[key].create(self.engine)

    def clear(self, log):
        while clear := self.session.query(TestUsers).filter_by(username=log).first():
            self.session.delete(clear)
        self.session_commit()
        assert not self.user_exist(log)

    def create_user(self, log, psw, email):
        self.clear(log)
        string = TestUsers(
            username=log,
            password=psw,
            email=email
        )            
        self.session.add(string)
        self.session_commit()

    def get_user(self, log):
        if self.user_exist(log):
            return self.session.query(TestUsers).filter_by(username=log).first()
        return None

    def user_exist(self, log):
        self.session_commit()
        return len(self.session.query(TestUsers).filter_by(username=log).all()) > 0

    def session_commit(self):
        try:    
            self.session.commit()
        except:
            self.session.rollback()
            self.session.commit()
