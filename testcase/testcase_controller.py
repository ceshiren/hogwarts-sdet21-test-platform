"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from flask import Flask, request
from flask_restx import Resource, Api, Namespace, fields

# 测试用例的接口层
from testcase.testcase_service import TestcaseService

testcase_ns = Namespace("testcase", description="测试用例管理")


# 接口路径定义到类上，对应的不同请求操作创建不同的方法
#
@testcase_ns.route("")
class Testcase(Resource):
    # restful 风格的 get 方法
    def get(self):
        case_id = request.args.get("id")
        testcase_service = TestcaseService()
        case_data = testcase_service.get_testcase(case_id)
        return {"code": 0, "msg": {"testcase": case_data}}

    testcases_docs = testcase_ns.model("testcase",
                      {
                          "type_id":fields.Integer,
                          "case_title":fields.String,
                          "case_info":fields.String,
                      })
    @testcase_ns.expect(testcases_docs)
    # restful 风格的 post 方法
    def post(self):
        return {"code": 0, "msg": "post success"}

    # restful 风格的 put 方法
    def put(self):
        return {"code": 0, "msg": "put success"}

    # restful 风格的 delete 方法
    def delete(self):
        return {"code": 0, "msg": "delete success"}


