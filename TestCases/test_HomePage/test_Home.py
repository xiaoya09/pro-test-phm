import os,jsonpath,json
from common.Loggoing import LoggerUtil
from common.SendRequests import Request
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml
from common.GetToken import GetToken

Authorization = GetToken().test_token()
HomePagePath=os.path.join(configYaml+'\HomePage.yaml')
HomePageDatas=Yaml_data().read_yaml(HomePagePath)

class Test_Home:
    def test_deviceIotStatistics(self):
        LoggerUtil().create_log().info("开始运行首页--设备概览统计用例：{}".format(HomePageDatas["deviceIotStatistics"]))
        headers={"Authorization":Authorization}
        res = Request().post_form_requests(conf.get("set", "test_url") +HomePageDatas["api_deviceIotStatistics"],data=HomePageDatas["paload"], headers=headers)
        res_dict=json.loads((res.text))
        total=res_dict.get("data")["total"]
        assert total==HomePageDatas["data"]["total"]



    def test_alarmInfo(self):
        LoggerUtil().create_log().info("开始运行首页---获取企业列表报警查询：{}".format(HomePageDatas["AlarmInfo"]))
        headers={"Authorization":Authorization}
        res = Request().get_requests(conf.get("set", "test_url") +HomePageDatas["api_AlarmInfo"], headers=headers)
        res_dict=json.loads((res.text))
        #将返回值的data里的所有name取出来
        names=jsonpath.jsonpath(res_dict,"$..name")
        #判断预期的企业名称是否在返回的列表里
        assert HomePageDatas["data_name"] in names



    def test_getNodeTree(self):
        LoggerUtil().create_log().info("开始运行首页---大屏列表下拉查询企业/服务：{}".format(HomePageDatas["getNodeTree"]))
        headers={"Authorization":Authorization}
        res = Request().get_requests(conf.get("set", "test_url") +HomePageDatas["api_getNodeTree"], headers=headers)
        res_dict=json.loads((res.text))
        #将返回值的data里的所有name取出来
        names=jsonpath.jsonpath(res_dict,"$..name")
        #判断预期的企业名称是否在返回的列表里
        assert HomePageDatas["data_name_01"] in names


    def test_query(self):
        LoggerUtil().create_log().info("开始运行首页---查询用户历史搜索关键字：{}".format(HomePageDatas["query"]))
        headers={"Authorization":Authorization}
        res = Request().get_requests(conf.get("set", "test_url") +HomePageDatas["api_query"], headers=headers)
        res_dict=json.loads((res.text))
        #将返回值的data里的所有历史id取出来
        names=jsonpath.jsonpath(res_dict,"$..id")
        #判断预期的企业名称是否在返回的列表里
        assert HomePageDatas["data_id"] in names



    def test_getScreenPostionInfo(self):
        LoggerUtil().create_log().info("开始运行首页---查询服务商、企业位置信息：{}".format(HomePageDatas["getScreenPostionInfo"]))
        headers={"Authorization":Authorization}
        res = Request().get_requests(conf.get("set", "test_url") +HomePageDatas["api_getScreenPostionInfo"], headers=headers)
        res_dict=json.loads((res.text))
        names=jsonpath.jsonpath(res_dict,"$..name")
        #判断预期的企业名称是否在返回的列表里
        assert HomePageDatas["name"] in names

    def test_realPlate(self):
        LoggerUtil().create_log().info("开始运行首页---实时看板：{}".format(HomePageDatas["realPlate"]))
        headers = {"Authorization": Authorization}
        res = Request().get_requests(conf.get("set", "test_url") + HomePageDatas["api_realPlate"],
                                     headers=headers)
        res_dict = json.loads((res.text))
        providerNumChain=res_dict.get("data")["providerNumChain"]
        assert providerNumChain==HomePageDatas["providerNumChain"]



    def test_enterAndDeviceNum(self):
        LoggerUtil().create_log().info("开始运行首页---接入数量：{}".format(HomePageDatas["enterAndDeviceNum"]))
        headers = {"Authorization": Authorization}
        res = Request().post_form_requests(conf.get("set", "test_url") + HomePageDatas["api_enterAndDeviceNum"],
                                     headers=headers)
        res_dict = json.loads((res.text))
        msg=res_dict.get("msg")
        assert msg==HomePageDatas["msg"]


    def test_list(self):
        LoggerUtil().create_log().info("开始运行首页---采集终端数列表：{}".format(HomePageDatas["list"]))
        headers = {"Content-Type":"application/json",
            "Authorization": Authorization}
        res = Request().post_json_requests(conf.get("set", "test_url") + HomePageDatas["api_list"],json=json.dumps(HomePageDatas["paload_list"]),
                                     headers=headers)
        res_dict=json.loads((res.text))
        enterpriseName=jsonpath.jsonpath(res_dict,"$..records[*].enterpriseName")
        assert HomePageDatas["enterpriseName"] in enterpriseName






if __name__ == '__main__':
    ll=Test_Home()
    ll.test_list()





