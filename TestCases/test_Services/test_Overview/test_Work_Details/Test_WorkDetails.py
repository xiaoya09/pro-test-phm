import os,jsonpath,json,allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml

Work_DetailsPath=os.path.join(configYaml+r'\ServiceDatas\Overview\Work_Details\WorkDetails.yaml')
Work_DetailsDatas=Yaml_data().read_yaml(Work_DetailsPath)



@allure.feature('工单模块')
class Test_Work_Details:

    @allure.story("工单类型统计")
    @allure.severity("normal")
    def test_queryWorkTypeNum(self):
        allure.dynamic.title("测试用例标题：%s" %(Work_DetailsDatas["queryWorkTypeNum"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + Work_DetailsDatas["api_queryWorkTypeNum"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Work_DetailsDatas["api_queryWorkTypeNum"], headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取data字段并转化为字符串"):
            data = jsonpath.jsonpath(res_dict, "$.data")
            dataStr="".join(map(str,data))
        with allure.step("第四步：判断data是否与预期相等"):
            assert Work_DetailsDatas["data"] == dataStr






    @allure.story("工单数据统计")
    @allure.severity("normal")
    def test_AllData(self):
        allure.dynamic.title("测试用例标题：%s" %(Work_DetailsDatas["AllData"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + Work_DetailsDatas["api_AllData"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Work_DetailsDatas["api_AllData"], headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取allPlan字段，转化为字符串---整型"):
            allPlan = jsonpath.jsonpath(res_dict, "$.data.allPlan")
            strAllPlan="".join(map(str,allPlan))
            intAllPlan=int(strAllPlan)
        with allure.step("第四步：判断allPlan与预期结果是否相等"):
            assert Work_DetailsDatas["allPlan"] == intAllPlan





    @allure.story("运维列表及服务评价")
    @allure.severity("normal")
    def test_list(self):
        allure.dynamic.title("测试用例标题：%s" %(Work_DetailsDatas["list"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") + Work_DetailsDatas["api_list"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Work_DetailsDatas["api_list"], json=json.dumps(Work_DetailsDatas["paload"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为字典格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：通过键值对获取pages字段，转化为字符串----整型"):
            pages = jsonpath.jsonpath(res_dict, "$.data.pages")
            pagesStr="".join(map(str,pages))
            intpages=int(pagesStr)
        with allure.step("第四步：判断pages与预期结果是否相等"):
            assert Work_DetailsDatas["allPlan"] == intpages