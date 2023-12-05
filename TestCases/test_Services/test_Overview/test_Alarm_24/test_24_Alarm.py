import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml

AlarmOverview_24_Path=os.path.join(configYaml+r'\ServiceDatas\Overview\24-hour\24H.yaml')
AlarmOverview_24_Datas=Yaml_data().read_yaml(AlarmOverview_24_Path)



"""
此测试类下的测试用例为大账号登录切换服务商进入总览--24小时活动报警的访问接口

"""

@allure.feature('24小时活动报警的访问接口')
class Test_Alarm:

    @allure.story("【24小时报警详情页统计】")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_alarmNumStatisticsTwentyFour(self):
        LoggerUtil().create_log().info("开始运行【24小时报警详情页统计】测试用例：{}".format(AlarmOverview_24_Datas["alarmNumStatisticsTwentyFour"]))
        headers = {"Content-Type":"application/json","Authorization":read_token_yaml() }
        res = Request().post_json_requests(
            conf.get("set", "test_url") + AlarmOverview_24_Datas["api_alarmNumStatisticsTwentyFour"],headers=headers)
        res_dict = json.loads((res.text))
        alarmStatusDesc = jsonpath.jsonpath(res_dict, "$.data[*].alarmStatusDesc")
        assert AlarmOverview_24_Datas["alarmStatusDesc"] in alarmStatusDesc




    @allure.story("【24小时报警详情趋势图】")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_alarmNumListTwentyFour(self):
        LoggerUtil().create_log().info("开始运行【24小时报警详情页趋势图】测试用例：{}".format(AlarmOverview_24_Datas["alarmNumListTwentyFour"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + AlarmOverview_24_Datas["api_alarmNumListTwentyFour"],json=json.dumps(AlarmOverview_24_Datas["paload"]),headers=headers)
        res_dict = json.loads((res.text))
        lowAlarmTwentyFour = jsonpath.jsonpath(res_dict, "$.data[*].lowAlarmTwentyFour")
        assert AlarmOverview_24_Datas["lowAlarmTwentyFour"] in lowAlarmTwentyFour



