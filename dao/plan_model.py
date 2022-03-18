"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.orm import Query, Session

db = SQLAlchemy("app")
db_session:Session = db.session




class PlanModel(db.Model):
    """
    数据库的操作
    """
    id = Column(Integer, primary_key=True)
    # project_id = db.Column(db.Integer, ForeignKey("project_models.id"))
    # scheduler_id = db.Column(db.Integer, ForeignKey("scheduler_models.id"))
    # filter_by = db.Column(db.JSON)
    # build = db.relationship("BuildModels", backref='plan_models',)
    # testcases = db.relationship('testcase_models',  secondary="plan_testcase_rel",
    #                             backref='plan_models', lazy=True)

    # def insert(*args, **kwargs):
    #     print(f"测试任务记录为{args}")

    @classmethod
    def create(cls, instance):
        db.session.add(instance)
        instance.save()

    @classmethod
    def get(cls):
        # cls.query.filter_by()
        # db.session
        # Query(cls).filter
        db_session.query(cls).filter_by()

    def save(self):
        db.session.commit()
        db.session.close()

    def delete(self):
        pass



