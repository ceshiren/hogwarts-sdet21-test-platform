"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from service.build import Build


class TestBuild:
    def setup_class(self):
        self.build = Build()
    def test_get(self):
        self.build.get(1)

    def test_create(self):
        self.build.create(1, "测试报告")



