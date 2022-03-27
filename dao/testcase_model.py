"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'

"""
# dao 层，只负责和数据库交互相关，供上层service调用。
from sqlalchemy import *

from backend_actual.log_util import logger
from server import db


class TestcaseModel(db.Model):
    # 表名
    __tablename__ = "testcase"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    case_title = db.Column(String(80), nullable=False, unique=True)
    # 备注
    remark = db.Column(String(120))

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def create(cls, case_id, case_title, remark):
        testcase = cls(id=case_id, case_title=case_title, remark=remark)
        logger.info(f"将要存储的内容为<======{testcase}")
        db.session.add(testcase)
        db.session.commit()
        db.session.close()

    @classmethod
    def delete(cls, **kwargs):
        TestcaseModel.query.filter_by(**kwargs).delete()
        # commit 之后需要添加close
        db.session.commit()
        db.session.close()  # 接口的返回信息
