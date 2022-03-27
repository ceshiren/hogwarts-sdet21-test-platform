"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from dao import testcase_plan_rel
from dao.build_model import BuildModel
from dao.plan_model import PlanModel
from dao.testcase_model import TestcaseModel

if __name__ == '__main__':
    from server import db
    # db.create_all()
    # db.drop_all()
#     testcase = TestcaseModel(case_title="test_demo.py", remark="111111")
#     testcase2 = TestcaseModel(case_title="test_demo2.py", remark="22222")
#     testcase3 = TestcaseModel(case_title="test_demo3.py", remark="33333")
#     db.session.add_all([testcase, testcase2, testcase3])
#     db.session.commit()
#     db.session.close()
#     plan1 = PlanModel(name="飞书计划")
#     db.session.add(plan1)
#     db.session.commit()
#
