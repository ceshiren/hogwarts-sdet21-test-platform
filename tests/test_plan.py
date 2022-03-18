"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from service.plan import Plan


class TestPlan:
    def setup_class(self):
        self.plan = Plan()

    def test_execute(self):
        r = self.plan.execute(suite_id=1, scheduler_type="mac")
        assert r

    def test_get(self):
        assert False

    def test_update(self):
        assert False

    def test_delete(self):
        assert False
