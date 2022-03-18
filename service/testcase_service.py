"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# service 层负责跨领域的，测试用例相关的业务逻辑

# 1.
from dao.testcase_dao import TestcaseDao


class TestcaseService:
    # 实例化对象操作
    def get_testcase(self, case_id):
        testcase = TestcaseDao()
        if case_id:
            testcase.query_by_id()
        else:
            testcase.query_all()
        return []