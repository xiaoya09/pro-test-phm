import os,jsonpath,json,allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml



OverviewPath=os.path.join(configYaml+r'\ServiceDatas\Overview\OverviewPage.yaml')
OverviewPathDatas=Yaml_data().read_yaml(OverviewPath)

@allure.feature('总览模块')
class Test_Overview_api:
    @allure.story("组态节点集合")
    @allure.severity("blocker")
    def test_nodeList(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["nodeList"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_nodeList"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_nodeList"],
            json=json.dumps(OverviewPathDatas["paload"]), headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的nodeName字段"):
            nodeName = jsonpath.jsonpath(res_dict, "$.data[*].nodeName")
        with allure.step("第四步：判断nodeName在不在列表里"):
            assert OverviewPathDatas["nodeName"] in nodeName






    @allure.story("设备概览统计")
    @allure.severity("blocker")
    def test_deviceIotStatistics(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["deviceIotStatistics"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_deviceIotStatistics"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_deviceIotStatistics"],
            json=json.dumps(OverviewPathDatas["paload_device"]), headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取total字段，然后转化为字符串--整型"):
            total = jsonpath.jsonpath(res_dict, "$.data.total")
            totalStr="".join(map(str,total))
            intTotal=int(totalStr)
        with allure.step("第四步：判断total是否与预期相等"):
            assert OverviewPathDatas["total"] == intTotal





    @allure.story("有未通报状态的高报、低保设备台数")
    @allure.severity("blocker")
    def test_returnDeviceNumber(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["returnDeviceNumber"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_returnDeviceNumber"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_returnDeviceNumber"],
            data=OverviewPathDatas["paload_returnDeviceNumber"], headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取alarmStatus字段"):
            alarmStatus = jsonpath.jsonpath(res_dict, "$..data[*].alarmStatus")
        with allure.step("第四步：判断alarmStatus在不在列表里"):
            assert OverviewPathDatas["alarmStatus"] in alarmStatus






    @allure.story("工单类型统计")
    @allure.severity("blocker")
    def test_queryWorkTypeNum(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["queryWorkTypeNum"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_queryWorkTypeNum"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_queryWorkTypeNum"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取data字段，并转化为字符串"):
            data = jsonpath.jsonpath(res_dict, "$..data")
            dataStr="".join(map(str,data))
        with allure.step("第四步：判断data与预期结果相等"):
            assert OverviewPathDatas["data"] == dataStr






    @allure.story("综合健康评分")
    @allure.severity("blocker")
    def test_score(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["score"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_score"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_score"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取logo字段，并转化为字符串"):
            logo = jsonpath.jsonpath(res_dict, "$..data.logo")
            logoStr="".join(map(str,logo))
        with allure.step("第四步：判断logo与预期结果相等"):
            assert OverviewPathDatas["logo"] == logoStr





    @allure.story("企业综合健康评分")
    @allure.severity("blocker")
    def test_enterprise_score(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["Enterprise_score"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_Enterprise_score"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_Enterprise_score"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取data字段，并转化为字符串"):
            data_score = jsonpath.jsonpath(res_dict, "$..data")
            data_scoreStr="".join(map(str,data_score))
        with allure.step("第四步：判断data与预期结果相等"):
            assert OverviewPathDatas["data_score"] == data_scoreStr





    @allure.story("维保概览首页展示")
    @allure.severity("blocker")
    def test_indexMain(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["indexMain"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_indexMain"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_indexMain"],json=json.dumps(OverviewPathDatas["paload_indexMain"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取data字段，并转化为字符串"):
            data_score = jsonpath.jsonpath(res_dict, "$..data")
            data_scoreStr="".join(map(str,data_score))
        with allure.step("第四步：判断data_score与预期结果相等"):
            assert OverviewPathDatas["data_score"] == data_scoreStr






    @allure.story("综合健康指数排名")
    @allure.severity("blocker")
    def test_ranking(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["ranking"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_ranking"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_ranking"],data=OverviewPathDatas["paload_ranking"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取enterpriseName字段"):
            enterpriseName = jsonpath.jsonpath(res_dict, "$..data.records[*].enterpriseName")
        with allure.step("第四步：判断enterpriseName在不在列表"):
            assert OverviewPathDatas["enterpriseName"] in  enterpriseName






    @allure.story("设备健康排名")
    @allure.severity("blocker")
    def test_device_ranking(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["device_ranking"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_device_ranking"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_device_ranking"],data=OverviewPathDatas["paload_device_ranking"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取pages字段，转化为字符串--整型"):
            pages = jsonpath.jsonpath(res_dict, "$..data.pages")
            pagesStr="".join(map(str,pages))
            intPages=int(pagesStr)
        with allure.step("第四步：判断pages与预期是否相等"):
            assert OverviewPathDatas["pages"] ==  intPages





    @allure.story("报警详情列表页")
    @allure.severity("blocker")
    def test_alarmRecordInfo(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["alarmRecordInfo"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_alarmRecordInfo"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_alarmRecordInfo"],json=json.dumps(OverviewPathDatas["paload_alarmRecordInfo"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取current字段，转化为字符串--整型"):
            current = jsonpath.jsonpath(res_dict, "$..data.current")
            currentStr="".join(map(str,current))
            intcurrent=int(currentStr)
        with allure.step("第四步：判断current与预期是否相等"):
            assert OverviewPathDatas["current"] ==  intcurrent






    @allure.story("获取默认视角")
    @allure.severity("blocker")
    def test_getDefaultView(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["getDefaultView"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_getDefaultView"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_getDefaultView"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取data字段，转化为字符串"):
            datas = jsonpath.jsonpath(res_dict, "$..data")
            datasStr="".join(map(str,datas))
        with allure.step("第四步：判断datas与预期是否相等"):
            assert OverviewPathDatas["datas"] ==  datasStr






    @allure.story("获取用户组件信息")
    @allure.severity("blocker")
    def test_info(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["info"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_info"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_info"],data=OverviewPathDatas["paload_info"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取level字段，转化为字符串--整型"):
            level = jsonpath.jsonpath(res_dict, "$..data.level")
            levelStr="".join(map(str,level))
            intLevel=int(levelStr)
        with allure.step("第四步：判断level与预期是否相等"):
            assert OverviewPathDatas["level"] ==  intLevel






    @allure.story("获取获取客户列表")
    @allure.severity("blocker")
    def test_list(self):
        allure.dynamic.title("测试用例标题：%s" %(OverviewPathDatas["list"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + OverviewPathDatas["api_list"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + OverviewPathDatas["api_list"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取enterpriseName字段"):
            enterpriseNamedatas = jsonpath.jsonpath(res_dict, "$..data[*].enterpriseName")
        with allure.step("第四步：判断enterpriseName在不在列表里"):
            assert OverviewPathDatas["enterpriseNamedatas"] in   enterpriseNamedatas




