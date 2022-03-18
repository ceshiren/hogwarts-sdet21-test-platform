"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# an Engine, which the Session will use for connection
# resources
engine = create_engine('postgresql://scott:tiger@localhost/')

Session1 = sessionmaker(engine)
session:Session = Session1()
