import os,jsonpath,json

from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml



OverviewPath=os.path.join(configYaml+r'\ServiceDatas\Overview\OverviewPage.yaml')
OverviewPathDatas=Yaml_data().read_yaml(OverviewPath)
"""
此测试类下的测试用例为大账号登录切换服务商进入总览页面的访问接口

"""

class Test_Overview_api:

    def test_nodeList(self):
        LoggerUtil().create_log().info("开始运行组态节点集合-nodeList测试用例：{}".format(OverviewPathDatas["nodeList"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_nodeList"],
            json=json.dumps(OverviewPathDatas["paload"]), headers=headers)
        res_dict = json.loads((res.text))
        nodeName = jsonpath.jsonpath(res_dict, "$.data[*].nodeName")
        # 返回的data数据是列表，将列表转换为字符串之后再转化为布尔类型
        assert OverviewPathDatas["nodeName"] in nodeName



    def test_deviceIotStatistics(self):
        LoggerUtil().create_log().info("开始运行设备概览统计测试用例：{}".format(OverviewPathDatas["deviceIotStatistics"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_deviceIotStatistics"],
            json=json.dumps(OverviewPathDatas["paload_device"]), headers=headers)
        res_dict = json.loads((res.text))
        total = jsonpath.jsonpath(res_dict, "$.data.total")
        totalStr="".join(map(str,total))
        intTotal=int(totalStr)
        # 返回的data数据是列表，将列表转换为字符串之后再转化为布尔类型
        assert OverviewPathDatas["total"] == intTotal


    def test_returnDeviceNumber(self):
        LoggerUtil().create_log().info("开始运行有未通报状态的高报、低保设备台数测试用例：{}".format(OverviewPathDatas["returnDeviceNumber"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_returnDeviceNumber"],
            data=OverviewPathDatas["paload_returnDeviceNumber"], headers=headers)
        res_dict = json.loads((res.text))
        alarmStatus = jsonpath.jsonpath(res_dict, "$..data[*].alarmStatus")
        assert OverviewPathDatas["alarmStatus"] in alarmStatus



    def test_queryWorkTypeNum(self):
        LoggerUtil().create_log().info("开始运行工单类型统计测试用例：{}".format(OverviewPathDatas["queryWorkTypeNum"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_queryWorkTypeNum"],headers=headers)
        res_dict = json.loads((res.text))
        data = jsonpath.jsonpath(res_dict, "$..data")
        dataStr="".join(map(str,data))
        assert OverviewPathDatas["data"] == dataStr




    def test_score(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看----综合健康评分测试用例：{}".format(OverviewPathDatas["score"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_score"],headers=headers)
        res_dict = json.loads((res.text))
        logo = jsonpath.jsonpath(res_dict, "$..data.logo")
        logoStr="".join(map(str,logo))
        assert OverviewPathDatas["logo"] == logoStr





    def test_enterprise_score(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---企业综合健康评分测试用例：{}".format(OverviewPathDatas["Enterprise_score"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_Enterprise_score"],headers=headers)
        res_dict = json.loads((res.text))
        data_score = jsonpath.jsonpath(res_dict, "$..data")
        data_scoreStr="".join(map(str,data_score))
        assert OverviewPathDatas["data_score"] == data_scoreStr




    def test_indexMain(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---维保概览首页展示测试用例：{}".format(OverviewPathDatas["indexMain"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_indexMain"],json=json.dumps(OverviewPathDatas["paload_indexMain"]),headers=headers)
        res_dict = json.loads((res.text))
        data_score = jsonpath.jsonpath(res_dict, "$..data")
        data_scoreStr="".join(map(str,data_score))
        assert OverviewPathDatas["data_score"] == data_scoreStr




    def test_ranking(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---综合健康指数排名测试用例：{}".format(OverviewPathDatas["ranking"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_ranking"],data=OverviewPathDatas["paload_ranking"],headers=headers)
        res_dict = json.loads((res.text))
        enterpriseName = jsonpath.jsonpath(res_dict, "$..data.records[*].enterpriseName")
        assert OverviewPathDatas["enterpriseName"] in  enterpriseName



    def test_device_ranking(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---设备健康排名测试用例：{}".format(OverviewPathDatas["device_ranking"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_device_ranking"],data=OverviewPathDatas["paload_device_ranking"],headers=headers)
        res_dict = json.loads((res.text))
        pages = jsonpath.jsonpath(res_dict, "$..data.pages")
        pagesStr="".join(map(str,pages))
        intPages=int(pagesStr)
        assert OverviewPathDatas["pages"] ==  intPages




    def test_alarmRecordInfo(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---报警详情列表页测试用例：{}".format(OverviewPathDatas["alarmRecordInfo"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_alarmRecordInfo"],json=json.dumps(OverviewPathDatas["paload_alarmRecordInfo"]),headers=headers)
        res_dict = json.loads((res.text))
        current = jsonpath.jsonpath(res_dict, "$..data.current")
        currentStr="".join(map(str,current))
        intcurrent=int(currentStr)
        assert OverviewPathDatas["current"] ==  intcurrent




    def test_getDefaultView(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---获取默认视角测试用例：{}".format(OverviewPathDatas["getDefaultView"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_getDefaultView"],headers=headers)
        res_dict = json.loads((res.text))
        datas = jsonpath.jsonpath(res_dict, "$..data")
        datasStr="".join(map(str,datas))
        assert OverviewPathDatas["datas"] ==  datasStr




    def test_info(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---获取用户组件信息测试用例：{}".format(OverviewPathDatas["info"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_info"],data=OverviewPathDatas["paload_info"],headers=headers)
        res_dict = json.loads((res.text))
        level = jsonpath.jsonpath(res_dict, "$..data.level")
        levelStr="".join(map(str,level))
        intLevel=int(levelStr)
        assert OverviewPathDatas["level"] ==  intLevel




    def test_list(self):
        LoggerUtil().create_log().info("开始运行admin账号登录查看---获取获取客户列表测试用例：{}".format(OverviewPathDatas["list"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_list"],headers=headers)
        res_dict = json.loads((res.text))
        enterpriseNamedatas = jsonpath.jsonpath(res_dict, "$..data[*].enterpriseName")
        assert OverviewPathDatas["enterpriseNamedatas"] in   enterpriseNamedatas




if __name__ == '__main__':
    ll = Test_Overview_api()
    ll.test_getDefaultView()
