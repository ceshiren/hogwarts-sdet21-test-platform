"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from plan.plan_dao import PlanDao
from scheduler.scheduler_service import SchedulerService
from suite.suite_service import SuiteService


class PlanService:
    def execute(self, data):
        # 1. 执行测试任务，把suite数据传给执行器
        # 2. 获取测试任务结果，如果成功执行，写入数据库
        # 3. 如果中间出现异常，抛出异常
        suite_id = data.get("suite_id")
        scheduler_type = data.get("scheduler")
        suite_service = SuiteService()
        suite_data = suite_service.get(suite_id)
        scheduler = SchedulerService()
        res = scheduler.execute(scheduler_type, suite_data)
        if res:
            # 测试任务执行成功。
            plan_dao = PlanDao()
            # 传入测试结果
            plan_dao.insert(suite_data)
        else:
            return False

        return True
