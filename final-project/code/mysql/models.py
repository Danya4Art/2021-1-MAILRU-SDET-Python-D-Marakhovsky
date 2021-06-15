from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TestUsers(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return  f"<\nid: '{self.id}'\n" \
                f"username: '{self.username}'\n" \
                f"password: '{self.password}'\n" \
                f"email: '{self.email}'\n" \
                f"access: {self.access}\n" \
                f"active: {self.active}\n" \
                f"start_active_time: {self.start_active_time}\n>"


    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(VARCHAR(16), unique=True, default=None)
    password = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(64), unique=True, nullable=False)
    access = Column(SmallInteger, default=None)
    active = Column(SmallInteger, default=None)
    start_active_time = Column(DateTime, default=None)
