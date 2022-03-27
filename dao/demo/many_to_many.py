"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from sqlalchemy import *
from sqlalchemy.orm import relationship

from server import db

# 中间表
testcase_plan_rel = db.Table(
    # 中间表的名称
    'testcase_plan_rel',
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('testcase_id', Integer,
           ForeignKey('testcase.id'),
           primary_key=True),
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('plan_id', Integer,
           ForeignKey('plan.id'),
           primary_key=True)
)

# 测试计划表
class PlanModel(db.Model):
    __tablename__ = "plan"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(80), nullable=False, unique=True)
    # 指向另外一张表， 另外一张表的类名， secondary 指向中间表的实例，
    # backref 反向指向
    testcases = relationship("TestcaseModel",
                             secondary=testcase_plan_rel,
                             backref="plancase")

# 用例表
class TestcaseModel(db.Model):
    # 表名
    __tablename__ = "testcase"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer,
                   primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空，并且唯一
    case_title = db.Column(String(80),
                           nullable=False, unique=True)
    remark = db.Column(String(120))

if __name__ == '__main__':
    # 多对多示例
    # db.create_all()
    db.drop_all()
    # =========数据的增加========
    # 1. 需要先有两张表的独立数据。
    # 2. 需要简历数据和数据之间的关联关系。
    # plan1 = PlanModel(name="飞书计划")
    # plan2 = PlanModel(name="企业微信计划")
    # plan3 = PlanModel(name="淘宝计划")
    testcase = TestcaseModel(case_title="test_demo.py", remark="111111")
    testcase2 = TestcaseModel(case_title="test_demo2.py", remark="22222")
    testcase3 = TestcaseModel(case_title="test_demo3.py", remark="33333")
    # # plan 表添加3条数据， testcase添加2条数据
    # db.session.add_all([plan1, plan2, plan3, testcase, testcase2, testcase3])
    # # 重点！！！！：建立关联关系
    # # 测试计划1 关联测试用例1，2
    # plan1.testcases = [testcase, testcase2]
    # # 测试用例3 关联测试计划2，3
    # testcase3.plancase = [plan2, plan3]
    # db.session.commit()
    # db.session.close()
    # =========数据的查询========
    # 查询测试用例3，对应的测试计划的名称
    # testcase3 = TestcaseModel.query.filter_by(id=3).first()
    # 获取测试用例3.的测试计划的第一个的名称
    # print(testcase3.plancase[0].name)
    # 查询测试计划，对应的所有的测试用例的case_title
    # plan3 = PlanModel.query.filter_by(id=3).first()
    # print(plan3.testcases[0].case_title)
    # =========数据的修改========
    # 1. 先查询，查询完成之后再修改
    # testcase3 = TestcaseModel.query.filter_by(id=3).first()
    # # 修改测试用例3.的测试计划的第一个的名称
    # testcase3.plancase[0].name = "企业微信计划2"
    # db.session.commit()
    # db.session.close()
    # testcase3 = TestcaseModel.query.filter_by(id=3).first()
    # 获取测试用例3.的测试计划的第一个的名称
    # print(testcase3.plancase[0].name)
    # =========数据的删除========
    # testcase2 = TestcaseModel.query.filter_by(id=2).first()
    # db.session.delete(testcase2)
    # db.session.commit()
    # db.session.close()


