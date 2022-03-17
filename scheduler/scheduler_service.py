"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from scheduler.scheduler_factory import SchedulerFactory


class SchedulerService:
    # todo: 抽象到domain
    def execute(self, scheduler_type, scheduler_data):
        scheduler = SchedulerFactory.scheduler_factory(scheduler_type)
        scheduler.execute(scheduler_data)

