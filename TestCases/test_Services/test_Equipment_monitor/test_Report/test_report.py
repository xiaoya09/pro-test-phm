import os,jsonpath,json, allure,pytest
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml


Report_Path=os.path.join(configYaml+r'\ServiceDatas\Equipment_pages_api\Diagnostic_Report\Report.yaml')
Report_PathDatas=Yaml_data().read_yaml(Report_Path)




@allure.feature("诊断报告")
class Test_Report:

    @allure.story("诊断报告列表")
    @allure.severity("critical")
    def test_listReport(self):
        allure.dynamic.title("测试用例标题：%s" % (Report_PathDatas["listReport"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Report_PathDatas["api_isEquipment"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Report_PathDatas["api_listReport"],json=json.dumps(Report_PathDatas["pload"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出usize字段"):
            size = jsonpath.jsonpath(res_dict, "$.data.size")
            strSize="".join(map(str,size))
            intSize=int(strSize)
        with allure.step("第四步：将取出来的size字段与预期做断言"):
            assert Report_PathDatas["size"] == intSize




    @allure.story("查询设备测点")
    @allure.severity("critical")
    def test_queryPoint(self):
        allure.dynamic.title("测试用例标题：%s" % (Report_PathDatas["queryPoint"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Report_PathDatas["api_isEquipment"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Report_PathDatas["api_queryPoint"],json=json.dumps(Report_PathDatas["ploads"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出deviceId字段,并转化为int"):
            deviceId = jsonpath.jsonpath(res_dict, "$.data.health.deviceId")
            strdeviceId="".join(map(str,deviceId))
            intdeviceId=int(strdeviceId)
        with allure.step("第四步：将取出来的deviceId字段与预期做断言"):
            assert Report_PathDatas["deviceId"] == intdeviceId




if __name__ == '__main__':
    pytest.main(["-s","test_report.py","--alluredir",r"D:\pythonProject\pro-test-phm\Outputs\tmp"])
    os.system("allure generate \pythonProject\pro-test-phm\\Outputs\\tmp  -o \pythonProject\pro-test-phm\\Outputs\\report ")