"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# from dao.plan_dao import PlanModel
from dao.plan_model import PlanModel
from service.scheduler_service import SchedulerService
from service.suite_service import SuiteService


class Plan:

    @classmethod
    def execute(cls, suite_id: int, scheduler_type):
        # 1. 执行测试计划，把suite数据传给执行器
        # 2. 获取测试任务结果，如果成功执行，写入数据库
        # 3. 如果中间出现异常，抛出异常
        suite_service = SuiteService()
        suite_data = suite_service.get(suite_id)
        scheduler = SchedulerService()
        res = scheduler.execute(scheduler_type, suite_data)
        if res:
            # 测试任务执行成功。
            plan_dao = PlanModel()
            # 传入测试结果
            plan_dao.save()
        else:
            return False
        return True

    def create(self):
        plan = PlanModel.create()

    def get(self):
        # PlanModel.query()
        # PlanModel.query
        plan_dao = PlanModel()
        # 传入测试结果
        plan_dao.get()

    def update(self):
        plan_dao = PlanModel()
        # 传入测试结果
        plan_dao.save()

    def delete(self):
        plan_dao = PlanModel()
        # 传入测试结果
        plan_dao.delete()

