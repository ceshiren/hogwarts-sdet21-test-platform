"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from sqlalchemy import *

from server import db

testcase_plan_rel = db.Table(
    # 中间表的名称
    'testcase_plan_rel',
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('testcase_id', Integer,
           ForeignKey('testcase.id'),
           primary_key=True),
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('plan_id', Integer,
           ForeignKey('plan.id'),
           primary_key=True)
)
