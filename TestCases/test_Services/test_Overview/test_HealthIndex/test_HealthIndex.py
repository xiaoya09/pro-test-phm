import os,jsonpath,json
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from TestCases.conftest import read_token_yaml
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request


Health_IndexPath=os.path.join(configYaml+r'\ServiceDatas\Overview\Health_Index_Details\Health_Index.yaml')
Health_IndexDatas=Yaml_data().read_yaml(Health_IndexPath)
"""
此测试类下的测试用例为大账号登录切换服务商进入总览--健康指数的访问接口

"""

class Test_Work_Details:

    def test_health_Index(self):
        LoggerUtil().create_log().info("开始运行健康问题词云测试用例：{}".format(Health_IndexDatas["cloud"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Health_IndexDatas["api_cloud"], headers=headers)
        res_dict = json.loads((res.text))
        name = jsonpath.jsonpath(res_dict, "$.data[*].name")
        assert Health_IndexDatas["name"] in name




    def test_list(self):
        LoggerUtil().create_log().info("开始运行设备健康列表测试用例：{}".format(Health_IndexDatas["list"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Health_IndexDatas["api_list"], headers=headers)
        res_dict = json.loads((res.text))
        Current = jsonpath.jsonpath(res_dict, "$.data.current")
        strCurrent="".join(map(str,Current))
        intCurrent=int(strCurrent)
        assert Health_IndexDatas["current"] == intCurrent