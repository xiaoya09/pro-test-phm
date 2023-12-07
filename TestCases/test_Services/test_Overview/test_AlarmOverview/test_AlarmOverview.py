import os,jsonpath,json,allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from TestCases.conftest import read_token_yaml
from common.Path_Send import configYaml
from common.SendRequests import Request


AlarmOverviewPath=os.path.join(configYaml+r'\ServiceDatas\Overview\AlarmOverview\AlarmOverview.yaml')
AlarmOverviewDatas=Yaml_data().read_yaml(AlarmOverviewPath)




@allure.feature('报警趋势图')
class Test_Alarm_Overview:
    @allure.story("报警概览详情页趋势图接口")
    @allure.severity("CRITICAL")
    def test_alarmNumList(self):
        allure.dynamic.title("测试用例标题：%s" %(AlarmOverviewDatas["alarmNumList"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + AlarmOverviewDatas["api_alarmNumList"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + AlarmOverviewDatas["api_alarmNumList"],json=json.dumps(AlarmOverviewDatas["paload"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的enterpriseId字段"):
            enterpriseId = jsonpath.jsonpath(res_dict, "$.data[*].enterpriseId")
        with allure.step("第四步：判断enterpriseId字段在不在列表里"):
            assert AlarmOverviewDatas["enterpriseId"] in enterpriseId
