"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from plan.plan_service import PlanService


class TestExecuteCase:
    def setup_class(self):
        self.plan = PlanService()

    def test_execute_suite(self):
        """
        通过指定suite执行用例
        :return:
        """
        self.plan.execute({"suite_id": 1, "scheduler": "mac"})