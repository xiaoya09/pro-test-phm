import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml

AlarmOverview_24_Path=os.path.join(configYaml+r'\ServiceDatas\Overview\24-hour\24H.yaml')
AlarmOverview_24_Datas=Yaml_data().read_yaml(AlarmOverview_24_Path)





@allure.feature('24小时活动报警的访问接口')
class Test_Alarm:

    @allure.story("24小时报警详情页统计")
    @allure.severity("CRITICAL")
    def test_alarmNumStatisticsTwentyFour(self):
        allure.dynamic.title("测试用例标题：%s" %(AlarmOverview_24_Datas["alarmNumStatisticsTwentyFour"]))
        headers = {"Content-Type":"application/json","Authorization":read_token_yaml() }
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + AlarmOverview_24_Datas["api_alarmNumStatisticsTwentyFour"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + AlarmOverview_24_Datas["api_alarmNumStatisticsTwentyFour"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的alarmStatusDesc字段"):
            alarmStatusDesc = jsonpath.jsonpath(res_dict, "$.data[*].alarmStatusDesc")
        with allure.step("第四步：判断alarmStatusDesc字段在不在列表里"):
            assert AlarmOverview_24_Datas["alarmStatusDesc"] in alarmStatusDesc






    @allure.story("24小时报警详情趋势图")
    @allure.severity("CRITICAL")
    def test_alarmNumListTwentyFour(self):
        allure.dynamic.title("测试用例标题：%s" %(AlarmOverview_24_Datas["alarmNumListTwentyFour"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + AlarmOverview_24_Datas["api_alarmNumListTwentyFour"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + AlarmOverview_24_Datas["api_alarmNumListTwentyFour"],json=json.dumps(AlarmOverview_24_Datas["paload"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的lowAlarmTwentyFour字段"):
            lowAlarmTwentyFour = jsonpath.jsonpath(res_dict, "$.data[*].lowAlarmTwentyFour")
        with allure.step("第四步：判断lowAlarmTwentyFour字段在不在列表里"):
            assert AlarmOverview_24_Datas["lowAlarmTwentyFour"] in lowAlarmTwentyFour



