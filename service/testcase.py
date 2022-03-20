"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 服务层
from backend_actual.log_util import logger
from dao.testcase_model import TestCase
from server import db


class Testcase:
    def get(self, case_id):
        if case_id:
            # 如果不为空，查询操作
            # case_data = TestCase.query.filter_by(id=case_id).first()
            case_data = TestCase.get_by_filter(id=case_id)
            logger.info(f"{case_data}")
            if case_data:
                datas = [{"id": case_data.id,
                          "case_title": case_data.case_title,
                          "remark": case_data.remark}]
                logger.info(f"要返回的数据为<======{datas}")
            else:
                datas = []
        else:
            # 为空，返回所有记录
            case_datas = TestCase.get_all()
            datas = [{"id": case_data.id,
                      "case_title": case_data.case_title,
                      "remark": case_data.remark} for case_data in case_datas]
        # return datas 保证路由有要返回的数据
        return datas

    def create(self,  case_id, case_title, remark):
        case_id = case_id
        # 查询数据库，查看是否有记录
        # exists = TestCase.query.filter_by(id=case_id).first()
        exists = TestCase.get_by_filter(id=case_id)
        logger.info(f"查询表结果：{exists}")
        if not exists:
            TestCase.create( case_id, case_title, remark)
            return True
        else:
            return False