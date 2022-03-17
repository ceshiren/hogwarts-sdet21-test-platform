"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from scheduler.MacScheduler import MacScheduler
from scheduler.jenkins_scheduler import JenkinsScheduler


class SchedulerFactory:
    @staticmethod
    def scheduler_factory(scheduler_name):
        if scheduler_name == "jenkins":
            return JenkinsScheduler()
        elif scheduler_name == "mac":
            return MacScheduler()