"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from jenkinsapi.jenkins import Jenkins

BASE_URL = "http://www.loseweight.ren:8080/" # Jenkins服务地址
USERNAME = "admin" # Jenkins的用户名
PASSWORD = "11226b92e460058bb05efc971b9fae92f8" # Jenkins用户的token
JOB = "python_ck"
jenkins_hogwarts = Jenkins(BASE_URL, USERNAME, PASSWORD)
print(jenkins_hogwarts.version)
# 获取jenkins的job对象
ck_job = jenkins_hogwarts.get_job(JOB)
# 构建job
ck_job.invoke()
# 获取当前job最后一次完成构建的编号
first_build_number = ck_job.get_last_buildnumber()
# build_params
ck_job.invoke(build_params={"task": "test"})



