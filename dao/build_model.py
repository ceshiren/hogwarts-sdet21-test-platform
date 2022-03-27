"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 构建记录
import datetime

from sqlalchemy import *

from server import db, db_session


class BuildModel(db.Model):
    # 表名
    __tablename__ = "build"
    # 构建id，主键
    id = db.Column(Integer, primary_key=True)
    # 外键指向测试计划的id
    plan_id = db.Column(Integer, ForeignKey("plan.id"))
    # 测试报告的链接
    report = db.Column(String(120), nullable=False, unique=True)
    # 创建时间，不需要传值，自动生成
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def create(cls, plan_id, report):
        instance = cls(plan_id=plan_id, report=report)
        db.session.add(instance)
        db.session.commit()
        db.session.close()

    @classmethod
    def get_all(cls):
        return db_session.query(cls).all()

    @classmethod
    def get_filter_by(cls, **kwargs):
        return db_session.query(cls).filter_by(**kwargs).all()