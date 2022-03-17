"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from suite.suite_dao import SuiteDao


class SuiteService:
    def __init__(self):
        self.suite_dao = SuiteDao()

    # 实例化对象操作
    def add(self, data):
        # 1. 将测试用例数据传入
        # 2. 完成逻辑判断
        # 3. 调用数据添加
        self.suite_dao.insert(data)
        return True

    def get(self, suite_id):
        if suite_id:
            return self.suite_dao.query_by_id(suite_id)
        else:
            return self.suite_dao.query_all()