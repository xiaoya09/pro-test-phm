import os,jsonpath,json
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from TestCases.conftest import read_token_yaml
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request


AlarmOverviewPath=os.path.join(configYaml+r'\ServiceDatas\Overview\AlarmOverview\AlarmOverview.yaml')
AlarmOverviewDatas=Yaml_data().read_yaml(AlarmOverviewPath)
"""
此测试类下的测试用例为大账号登录切换服务商进入总览--报警概览页面的访问接口

"""

class Test_Alarm_Overview:

    def test_alarmNumList(self):
        LoggerUtil().create_log().info("开始运行报警概览详情页趋势图测试用例：{}".format(AlarmOverviewDatas["alarmNumList"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + AlarmOverviewDatas["api_alarmNumList"],json=json.dumps(AlarmOverviewDatas["paload"]),headers=headers)
        res_dict = json.loads((res.text))
        enterpriseId = jsonpath.jsonpath(res_dict, "$.data[*].enterpriseId")
        assert AlarmOverviewDatas["enterpriseId"] in enterpriseId
