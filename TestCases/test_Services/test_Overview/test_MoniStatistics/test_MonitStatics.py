import os,jsonpath,json
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from TestCases.conftest import read_token_yaml
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request


MonitStatisticsPath=os.path.join(configYaml+r'\ServiceDatas\Overview\MonitoringStatistics\MonitStatistics.yaml')
MonitStatisticsDatas=Yaml_data().read_yaml(MonitStatisticsPath)
"""
此测试类下的测试用例为大账号登录切换服务商进入总览--监测统计页面的访问接口

"""

class Test_MonitStatis:

    def test_statusNumList(self):
        LoggerUtil().create_log().info("开始运行设备概览详情页趋势图-statusNumList测试用例：{}".format(MonitStatisticsDatas["statusNumList"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + MonitStatisticsDatas["api_statusNumList"],json=json.dumps(MonitStatisticsDatas["paload"]), headers=headers)
        res_dict = json.loads((res.text))
        enterpriseId = jsonpath.jsonpath(res_dict, "$.data[*].enterpriseId")
        assert MonitStatisticsDatas["enterpriseId"] in enterpriseId



    def test_optionselect(self):
        LoggerUtil().create_log().info("开始运行获取客户下拉框列表测试用例：{}".format(MonitStatisticsDatas["optionselect"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + MonitStatisticsDatas["api_optionselect"],headers=headers)
        res_dict = json.loads((res.text))
        enterpriseName = jsonpath.jsonpath(res_dict, "$.data[*].enterpriseName")
        assert MonitStatisticsDatas["enterpriseName"] in enterpriseName





    def test_allList(self):
        LoggerUtil().create_log().info("开始运行查询设备所有分类列表测试用例：{}".format(MonitStatisticsDatas["allList"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + MonitStatisticsDatas["api_allList"],headers=headers)
        res_dict = json.loads((res.text))
        createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        assert MonitStatisticsDatas["createBy"] in createBy






if __name__ == '__main__':
    ll = Test_MonitStatis()
    ll.test_statusNumList()