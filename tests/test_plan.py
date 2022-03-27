"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from service.plan import Plan


class TestPlan:
    def setup_class(self):
        self.plan = Plan()

    def test_create(self):
        self.plan.create("测试计划3", [1])

    def test_get(self):
        self.plan.get(1)
        # assert False
