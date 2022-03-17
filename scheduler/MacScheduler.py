"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os


class MacScheduler:
    def execute(self,scheduler_data):
        # {
        # "suite_name": "wechat",
        # "cases_data": [{"case_id": 1, "command": "test_demo.py"}, ]}

        case_data = scheduler_data.get("cases_data")
        commands = [case.get("command") for case in case_data]
        command_str = " ".join(commands)
        print(f"构建命令为{command_str}")
        os.system(command_str)



