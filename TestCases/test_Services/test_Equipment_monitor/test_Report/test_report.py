import os,jsonpath,json, allure,pytest
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml


Report_Path=os.path.join(configYaml+r'\ServiceDatas\Equipment_pages_api\Diagnostic_Report\Report.yaml')
Report_PathDatas=Yaml_data().read_yaml(Report_Path)
"""
此测试类下的测试用例为大账号登录切换服务商进入设备监测--诊断报告

"""

@allure.feature("诊断报告")
class Test_Report:

    @allure.story("诊断报告列表")
    def test_listReport(self):
        LoggerUtil().create_log().info("开始运行诊断报告列表测试用例：{}".format(Report_PathDatas["listReport"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Report_PathDatas["api_listReport"],json=json.dumps(Report_PathDatas["pload"]),headers=headers)
        res_dict = json.loads((res.text))
        size = jsonpath.jsonpath(res_dict, "$.data.size")
        strSize="".join(map(str,size))
        intSize=int(strSize)
        assert Report_PathDatas["size"] == intSize



    @allure.story("查询设备测点")
    def test_queryPoint(self):
        LoggerUtil().create_log().info("开始运行查询设备测点测试用例：{}".format(Report_PathDatas["queryPoint"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Report_PathDatas["api_queryPoint"],json=json.dumps(Report_PathDatas["ploads"]),headers=headers)
        res_dict = json.loads((res.text))
        deviceId = jsonpath.jsonpath(res_dict, "$.data.health.deviceId")
        strdeviceId="".join(map(str,deviceId))
        intdeviceId=int(strdeviceId)
        assert Report_PathDatas["deviceId"] == intdeviceId




if __name__ == '__main__':
    pytest.main(["-s","test_report.py","--alluredir",r"D:\pythonProject\pro-test-phm\Outputs\tmp"])
    os.system("allure generate \pythonProject\pro-test-phm\\Outputs\\tmp  -o \pythonProject\pro-test-phm\\Outputs\\report ")