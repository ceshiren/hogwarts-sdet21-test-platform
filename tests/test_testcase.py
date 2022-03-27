"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from service.testcase import Testcase


class TestTestcase:
    """
    先编写单元测试，再编写业务逻辑TDD
    """
    def setup_class(self):
        self.testcase = Testcase()

    def test_get(self):
        r = self.testcase.get()
        assert r != []


    def test_create(self):
        self.testcase.create(3, "test_wework_case.py", "接口测试用例")
        # 如果create 方法没有bug，那么使用get(5)，就一定有返回值
        r = self.testcase.get(3)
        # 相当于一个后置动作，只是为了方便单元测试
        # self.testcase.delete(6)
        assert r != []

    def test_delete(self):
        self.testcase.delete(1)
        r = self.testcase.get(1)
        # 断言获取到的结果为空，表示删除成功
        assert r == []
