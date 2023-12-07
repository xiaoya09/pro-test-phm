import os,jsonpath,json,allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from TestCases.conftest import read_token_yaml
from common.Path_Send import configYaml
from common.SendRequests import Request


MonitStatisticsPath=os.path.join(configYaml+r'\ServiceDatas\Overview\MonitoringStatistics\MonitStatistics.yaml')
MonitStatisticsDatas=Yaml_data().read_yaml(MonitStatisticsPath)

@allure.feature('监测统计模块')
class Test_MonitStatis:

    @allure.story("设备概览详情页趋势图")
    @allure.severity("CRITICAL")
    def test_statusNumList(self):
        allure.dynamic.title("测试用例标题：%s" %(MonitStatisticsDatas["statusNumList"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + MonitStatisticsDatas["api_statusNumList"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + MonitStatisticsDatas["api_statusNumList"],json=json.dumps(MonitStatisticsDatas["paload"]), headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的enterpriseId字段"):
            enterpriseId = jsonpath.jsonpath(res_dict, "$.data[*].enterpriseId")
        with allure.step("第四步：判断enterpriseId字段在不在列表里"):
            assert MonitStatisticsDatas["enterpriseId"] in enterpriseId





    @allure.story("获取客户下拉框列表")
    @allure.severity("CRITICAL")
    def test_optionselect(self):
        allure.dynamic.title("测试用例标题：%s" %(MonitStatisticsDatas["optionselect"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + MonitStatisticsDatas["api_optionselect"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + MonitStatisticsDatas["api_optionselect"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的enterpriseName字段"):
            enterpriseName = jsonpath.jsonpath(res_dict, "$.data[*].enterpriseName")
        with allure.step("第四步：判断enterpriseName字段在不在列表里"):
            assert MonitStatisticsDatas["enterpriseName"] in enterpriseName






    @allure.story("获取客户下拉框列表")
    @allure.severity("CRITICAL")
    def test_allList(self):
        allure.dynamic.title("测试用例标题：%s" %(MonitStatisticsDatas["allList"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + MonitStatisticsDatas["api_allList"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + MonitStatisticsDatas["api_allList"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的createBy字段"):
            createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        with allure.step("第四步：判断createBy字段在不在列表里"):
            assert MonitStatisticsDatas["createBy"] in createBy






