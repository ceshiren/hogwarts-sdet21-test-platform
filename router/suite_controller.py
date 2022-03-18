"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


from flask import request
from flask_restx import Resource, Namespace, fields

from service.suite_service import SuiteService

suite_ns = Namespace("testcase", description="测试用例管理")



# 接口路径定义到类上，对应的不同请求操作创建不同的方法
@suite_ns.route("")
class SuiteController(Resource):
    # restful 风格的 get 方法
    def get(self):
        suite_id = request.args.get("id")
        suite_service = SuiteService()
        suite_data = suite_service.get(suite_id)
        return {"code": 0, "msg": {"suite": suite_data}}

    suite_docs = suite_ns.model("suite",
                      {
                          "id":fields.Integer,
                      })
    @suite_ns.expect(suite_docs)
    # restful 风格的 post 方法
    def post(self):
        # 1. 选择测试用例，点击新增测试suite
        # 2. 传入用例信息
        case_data = request.json.get("testcase")
        suite_service = SuiteService()
        suite_service.add(case_data)

        return {"code": 0, "msg": "post success"}

    # restful 风格的 put 方法
    def put(self):
        return {"code": 0, "msg": "put success"}

    # restful 风格的 delete 方法
    def delete(self):
        return {"code": 0, "msg": "delete success"}


