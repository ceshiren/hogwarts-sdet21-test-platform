"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from backend_actual.log_util import logger


class Build:

    def get(self):
        pass

    def create(self, plan_id, testcase_info):
        """

        :param plan_id:
        :param testcase:
        :return:
        """
        logger.info(f"测试计划{plan_id}执行了测试用例{testcase_info}")