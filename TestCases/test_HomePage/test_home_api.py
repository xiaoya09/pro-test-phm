import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml

HomePages_Path=os.path.join(configYaml+r'\HomePage.yaml')
HomePages_Datas=Yaml_data().read_yaml(HomePages_Path)


@allure.feature('首页接口')
class Test_HomePage:

    @allure.story("设备概览统计")
    @allure.severity("CRITICAL")
    def test_deviceIotStatistics(self):
        allure.dynamic.title("测试用例标题：%s" %(HomePages_Datas["title"]))
        headers = {"Authorization":read_token_yaml() }
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + HomePages_Datas["api_deviceIotStatistics"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + HomePages_Datas["api_deviceIotStatistics"],data=HomePages_Datas["paload"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取total字段,转化为字符串--整型"):
            total = jsonpath.jsonpath(res_dict, "$.data.total")
            strtotal="".join(map(str,total))
            intTotal=int(strtotal)
        with allure.step("第四步：判断total是否与预期结果相等"):
            assert HomePages_Datas["total"] == intTotal






    @allure.story("获取企业列表报警查询")
    @allure.severity("CRITICAL")
    def test_AlarmInfo(self):
        allure.dynamic.title("测试用例标题：%s" % (HomePages_Datas["AlarmInfo"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(
                conf.get("set", "test_url") + HomePages_Datas["api_AlarmInfo"])):
            res = Request().get_requests(
                conf.get("set", "test_url") + HomePages_Datas["api_AlarmInfo"],
                headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的data_name字段"):
            data_name = jsonpath.jsonpath(res_dict, "$.data[*].name")
        with allure.step("第四步：判断data_name是否在列表里"):
            assert HomePages_Datas["data_name"] in data_name





    @allure.story("大屏列表下拉查询企业/服务")
    @allure.severity("CRITICAL")
    def test_getNodeTree(self):
        allure.dynamic.title("测试用例标题：%s" % (HomePages_Datas["getNodeTree"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(
                conf.get("set", "test_url") + HomePages_Datas["api_getNodeTree"])):
            res = Request().get_requests(
                conf.get("set", "test_url") + HomePages_Datas["api_getNodeTree"],
                headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的data_name字段"):
            data_name = jsonpath.jsonpath(res_dict, "$.data[*].name")
        with allure.step("第四步：判断data_name是否在列表里"):
            assert HomePages_Datas["data_name_01"] in data_name






    @allure.story("查询用户历史搜索关键字")
    @allure.severity("CRITICAL")
    def test_query(self):
        allure.dynamic.title("测试用例标题：%s" % (HomePages_Datas["query"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(
                conf.get("set", "test_url") + HomePages_Datas["api_query"])):
            res = Request().get_requests(
                conf.get("set", "test_url") + HomePages_Datas["api_query"],
                headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的id字段"):
            id = jsonpath.jsonpath(res_dict, "$.data[*].id")
        with allure.step("第四步：判断id是否在列表里"):
            assert HomePages_Datas["data_id"] in id






    @allure.story("查询服务商、企业位置信息")
    @allure.severity("CRITICAL")
    def test_query(self):
        allure.dynamic.title("测试用例标题：%s" % (HomePages_Datas["getScreenPostionInfo"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(
                conf.get("set", "test_url") + HomePages_Datas["api_getScreenPostionInfo"])):
            res = Request().get_requests(
                conf.get("set", "test_url") + HomePages_Datas["api_getScreenPostionInfo"],
                headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的name字段"):
            name = jsonpath.jsonpath(res_dict, "$.data[*].name")
        with allure.step("第四步：判断id是否在列表里"):
            assert HomePages_Datas["name"] in name





    @allure.story("实时看板")
    @allure.severity("CRITICAL")
    def test_realPlate(self):
        allure.dynamic.title("测试用例标题：%s" % (HomePages_Datas["realPlate"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(
                conf.get("set", "test_url") + HomePages_Datas["api_realPlate"])):
            res = Request().get_requests(
                conf.get("set", "test_url") + HomePages_Datas["api_realPlate"],
                headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的providerNumChain字段"):
            providerNumChain = jsonpath.jsonpath(res_dict, "$.data.providerNumChain")
            strproviderNumChain="".join(map(str,providerNumChain))
        with allure.step("第四步：判断providerNumChain是否与预期结果相等"):
            assert HomePages_Datas["providerNumChain"] == strproviderNumChain






    @allure.story("接入数量")
    @allure.severity("CRITICAL")
    def test_enterAndDeviceNum(self):
        allure.dynamic.title("测试用例标题：%s" % (HomePages_Datas["enterAndDeviceNum"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(
                conf.get("set", "test_url") + HomePages_Datas["api_enterAndDeviceNum"])):
            res = Request().post_form_requests(
                conf.get("set", "test_url") + HomePages_Datas["api_enterAndDeviceNum"],
                headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取msg字段"):
            msg = jsonpath.jsonpath(res_dict, "$.msg")
            strmsg="".join(map(str,msg))
        with allure.step("第四步：判断strmsg是否与预期结果相等"):
            assert HomePages_Datas["msg"] == strmsg






    @allure.story("采集终端数列表")
    @allure.severity("CRITICAL")
    def test_list(self):
        allure.dynamic.title("测试用例标题：%s" % (HomePages_Datas["list"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(
                conf.get("set", "test_url") + HomePages_Datas["api_list"])):
            res = Request().post_json_requests(
                conf.get("set", "test_url") + HomePages_Datas["api_list"],json=json.dumps(HomePages_Datas["paload_list"]),
                headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取enterpriseName字段"):
            enterpriseName = jsonpath.jsonpath(res_dict, "$.data.records[*].enterpriseName")
            print(enterpriseName)
        with allure.step("第四步：判断enterpriseName是否在列表里"):
            assert HomePages_Datas["enterpriseName"] in enterpriseName




