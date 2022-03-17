"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
class JenkinsScheduler:
    def execute(self,scheduler_data):
        """
        1. 生成一个jenkins job
        2. 构建任务
        3. 回传报告
        :return:
        """
        print(f"构建的任务id为->1，报告地址为{scheduler_data}")
