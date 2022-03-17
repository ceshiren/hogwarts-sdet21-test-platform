"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


from flask import Flask, request
from flask_restx import Resource, Api, Namespace, fields

from plan.plan_service import PlanService

plan_ns = Namespace("testcase", description="测试用例管理")





@plan_ns.route("")
class PlanController(Resource):
    # restful 风格的 get 方法
    def get(self):
        # 测试计划记录
        return {"code": 0, "msg": {"plan": "plan"}}


    plan_docs = plan_ns.model("plan",
                      {
                          "id":fields.Integer,
                      })
    @plan_ns.expect(plan_docs)
    # restful 风格的 post 方法
    def post(self):
        plan_data = request.json.get("data")
        plan_service = PlanService()
        res = plan_service.execute(plan_data)
        return {"code": 0, "msg": res}

    # restful 风格的 put 方法
    def put(self):
        return {"code": 0, "msg": "put success"}

    # restful 风格的 delete 方法
    def delete(self):
        return {"code": 0, "msg": "delete success"}


