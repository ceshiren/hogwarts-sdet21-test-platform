"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import request

from backend_actual.log_util import logger
from server import api
from flask_restx import Resource, Api, Namespace

case_ns = Namespace("case", description="用例管理")

@case_ns.route("")
class TestCaseServer(Resource):
    get_paresr = api.parser()
    # 查询接口， 可以传id ，也可以不传id，
    # 不传id：就是返回 全部记录
    # 传id：返回查询到的对应的记录，如果未查到则返回 空列表
    get_paresr.add_argument("id", type=int, location="args")

    @case_ns.expect(get_paresr)
    def get(self):
        """
        测试用例的查找
        :return:
        """
        case_id = request.args.get("id")
        logger.info(f"type(request.args) <===== {type(request.args)}")
        logger.info(f"接收到的参数 <===== {case_id}")
        return {"code": 0, "msg": f"1111"}

    post_paresr = api.parser()
    post_paresr.add_argument("id", type=int, required=True, location="json")
    post_paresr.add_argument("case_title", type=str, required=True, location="json")
    post_paresr.add_argument("remark", type=str, location="json")
    @case_ns.expect(post_paresr)
    def post(self):
        """
        测试用例的新增
        :return:
        """
        # 获取请求数据
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        return {"code": 0, "msg": f"case id success add."}

    put_paresr = api.parser()
    put_paresr.add_argument("id", type=int, required=True, location="json")
    put_paresr.add_argument("case_title", type=str, required=True, location="json")
    put_paresr.add_argument("remark", type=str, location="json")
    @case_ns.expect(put_paresr)
    def put(self):
        """
        测试用例的修改
        :return:
        """
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        return {"code": 0, "msg": f"case put"}


    delete_parser = api.parser()
    delete_parser.add_argument("id", type=int, location="json", required=True)
    @case_ns.expect(delete_parser)
    def delete(self):
        """
        测试用例的删除
        :return:
        """
        case_data = request.json
        case_id = case_data.get("id")
        logger.info(f"接收到的参数id <====={case_id}")
        return {"code": 0, "msg": f"case delete"}


