"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from jenkinsapi.jenkins import Jenkins

class JenkinsUtils:

    BASE_URL = "http://www.loseweight.ren:8080/" # Jenkins服务地址
    USERNAME = "admin" # Jenkins的用户名
    PASSWORD = "11d4051dbc3cc66c2fbfcd7bb5772f7ae9" # Jenkins用户的token
    JOB = "ck21"

    @classmethod
    def invoke(cls, **kwargs):
        jenkins_hogwarts = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 获取jenkins的job对象
        ck_job = jenkins_hogwarts.get_job(cls.JOB)
        # 构建job
        # 获取当前job最后一次完成构建的编号
        # build_params
        ck_job.invoke(build_params=kwargs)
        first_build_number = ck_job.get_last_buildnumber()
        # 获取测试报告的多种方式
        # 1. 自己解析测试报告数据，自己完成测试报告的UI模板展示。渲染到前端生成
        # 2. 直接使用allure的测试报告
#       http://www.loseweight.ren:8080/job/ck21/13/allure/
        report = f"{cls.BASE_URL}job/{cls.JOB}/{first_build_number+1}/allure"
        return report



if __name__ == '__main__':
    JenkinsUtils.invoke(task="test_wework_case.py")

