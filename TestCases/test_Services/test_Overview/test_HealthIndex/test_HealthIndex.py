import os,jsonpath,json,allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from TestCases.conftest import read_token_yaml
from common.Path_Send import configYaml
from common.SendRequests import Request


Health_IndexPath=os.path.join(configYaml+r'\ServiceDatas\Overview\Health_Index_Details\Health_Index.yaml')
Health_IndexDatas=Yaml_data().read_yaml(Health_IndexPath)

@allure.feature('健康指数')
class Test_Work_Details:
    @allure.story("健康问题词云")
    @allure.severity("normal")
    def test_health_Index(self):
        allure.dynamic.title("测试用例标题：%s" %(Health_IndexDatas["cloud"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + Health_IndexDatas["api_cloud"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Health_IndexDatas["api_cloud"], headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的name字段"):
            name = jsonpath.jsonpath(res_dict, "$.data[*].name")
        with allure.step("第四步：判断name字段在不在列表里"):
            assert Health_IndexDatas["name"] in name






    @allure.story("健康问题词云")
    @allure.severity("normal")
    def test_list(self):
        allure.dynamic.title("测试用例标题：%s" %(Health_IndexDatas["list"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") + Health_IndexDatas["api_list"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Health_IndexDatas["api_list"], headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取所有的current字段"):
            Current = jsonpath.jsonpath(res_dict, "$.data.current")
        with allure.step("第四步：将current转化为字符串，在转化整数"):
            strCurrent="".join(map(str,Current))
            intCurrent=int(strCurrent)
        with allure.step("第五步：判断current与实际current是否相等"):
            assert Health_IndexDatas["current"] == intCurrent