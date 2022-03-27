"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from backend_actual.log_util import logger
from dao import TestcaseModel, PlanModel
from server import db_session
from service.build import Build
from utils.jenkins_util import JenkinsUtils


class Plan:

    def execute(self, plan_id, case_titles):
        """
        执行测试用例， 需要传入计划的id，以及对应的具体的用例信息
        test_demo.py
        :return:
        """

        # ['testcase1.py', 'testcase2.py']  -> pytest testcase1.py testcase2.py
        # 完成格式转换，jenkins可以直接调用
        case_titles = " ".join(case_titles)
        logger.debug(f"测试计划{plan_id}，"
                     f"要执行的的测试用例内容{case_titles}")
        # 调用执行器执行测试用例
        report = JenkinsUtils.invoke(task=case_titles)
        # 写入构建记录
        build = Build()
        build.create(plan_id, report)


    def create(self, name, case_id_lists):
        """
        1. 获得关联的测试用例，创建对应的测试计划
        2. 执行测试计划，生成一条构建记录
            1. 执行了那些用例
            2. 关联的测试计划是什么
        :return:
        """
        # case_id_lists -> case_objs

        case_objects = [TestcaseModel.get_by_filter(id = case_id)
                        for case_id in case_id_lists]
        logger.debug(f"测试列表{case_id_lists}，"
                     f"获取到的测试用例的对象为{case_objects}")
        # 在创建的过程中，需要传入测试计划的名称，并且指出关联那些测试用例
        plan_id = PlanModel.create(name, case_objects)
        # 直接调用get方法，获取转换后的测试数据的格式
        case_titles = self.get(plan_id)[0]["testcase_info"]
        self.execute(plan_id, case_titles)



    def get(self, plan_id=None):
        """

        :param plan_id:
        :return:
        """

        plan_objects = self.get_objs(plan_id)
        plan_datas = [{"id":plan_object.id,
                       "name": plan_object.name,
                       # 获取到的测试数据从对象转换成实际的数据信息，方便阅读
                       "testcase_info": [
                           testcase.case_title for testcase in plan_object.testcases] }
                      for plan_object in plan_objects]
        logger.info(f"获取到的测试计划的数据为->{plan_datas}")
        return plan_datas


    def get_objs(self, plan_id=None):
        if plan_id:
            r = PlanModel.get_filter_by(id=plan_id)
        else:
            r = PlanModel.get_all()
        logger.debug(f"获取到的测试计划的列表为{r}")
        return r