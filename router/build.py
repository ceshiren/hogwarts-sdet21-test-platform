"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import request
from flask_restx import Namespace, Resource

from backend_actual.log_util import logger
from server import api
from service.build import Build

build_ns = Namespace("build", description="构建记录管理")


@build_ns.route("")
class BuildServer(Resource):
    get_paresr = api.parser()
    # 查询接口， 可以传id ，也可以不传id，
    # 不传id：就是返回 全部记录
    # 传id：返回查询到的对应的记录，如果未查到则返回 空列表
    get_paresr.add_argument("plan_id", type=int, location="args")
    @build_ns.expect(get_paresr)
    def get(self):
        """
        构建记录的查找
        :return:
        """
        # 接口的请求数据信息
        plan_id = request.args.get("id")
        logger.info(f"测试计划获取接口接收到的参数 <===== {plan_id}")
        # =====调用service层的具体的业务逻辑
        build = Build()
        datas = build.get(plan_id)
        # ====
        # 给接口的响应内容
        return {"code": 0, "msg": {"status": "success", "data": datas}}

    # post_paresr = api.parser()
    # post_paresr.add_argument("name", type=str, required=True, location="json")
    # post_paresr.add_argument("testcases", location="json")
    # @build_ns.expect(post_paresr)
    # def post(self):
    #     """
    #     goujian
    #     :return:
    #     """
    #     # 获取请求数据
    #     build_data = request.json
    #     logger.info(f"测试计划新增接口接收到的参数<====== {build_data}")
    #     name = build_data.get("name")
    #     testcases = build_data.get("testcases")
    #     # ===============调用的service逻辑
    #     build = Build()
    #     build.create(name, testcases)
    #     return {"code": 0, "msg": f"build success add."}
