from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Lenght(Base):
    __tablename__ = 'lenght'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"num: {self.num}"

    num = Column(Integer, primary_key=True)


class Types(Base):
    __tablename__ = 'types'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"request: '{self.req}'\tcount: {self.count}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    req = Column(String(300), nullable=False)
    count =  Column(Integer, nullable=False)


class Count(Base):
    __tablename__ = 'count'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"count: {self.count}\turl: '{self.url}'"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)
    url = Column(String(300), nullable=False)


class Val(Base):
    __tablename__ = 'val'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return  f"<url: '{self.url}'\n" \
                f"code: {self.code}\n" \
                f"value: {self.val}\n" \
                f"ip: {self.ip}>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    code = Column(Integer, nullable=False)
    val = Column(Integer, nullable=False)
    ip = Column(String(15),  nullable=False)


class Error(Base):
    __tablename__ = 'error'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"ip: {self.ip}\tcount: {self.count}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    count = Column(Integer, nullable=False)
