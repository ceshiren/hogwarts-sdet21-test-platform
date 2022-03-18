"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
class SuiteDao:

    def insert(self, data):
        return True

    def query_all(self):
        return []

    def query_by_id(self, id):
        return {
            "suite_name": "wechat",
            "cases_data": [
                {"case_id": 1, "command": "pytest ./tests/test_demo.py"},
            ]
        }

    def delete(self, suite_id=None):
        return True
