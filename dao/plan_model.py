"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 测试计划
from sqlalchemy import *
from sqlalchemy.orm import relationship

from dao import testcase_plan_rel
from server import db


class PlanModel(db.Model):
    # 表名
    __tablename__ = "plan"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 测试计划的名称
    name = db.Column(String(80), nullable=False, unique=True)
    # 引用测试用例的属性
    testcases = relationship("TestcaseModel",
                             secondary=testcase_plan_rel,
                             backref="plancase")

