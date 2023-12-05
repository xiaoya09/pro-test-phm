import os,jsonpath,json
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml

Work_DetailsPath=os.path.join(configYaml+r'\ServiceDatas\Overview\Work_Details\WorkDetails.yaml')
Work_DetailsDatas=Yaml_data().read_yaml(Work_DetailsPath)
"""
此测试类下的测试用例为大账号登录切换服务商进入总览--工单详情的访问接口

"""

class Test_Work_Details:

    def test_queryWorkTypeNum(self):
        LoggerUtil().create_log().info("开始运行工单类型统计测试用例：{}".format(Work_DetailsDatas["queryWorkTypeNum"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Work_DetailsDatas["api_queryWorkTypeNum"], headers=headers)
        res_dict = json.loads((res.text))
        data = jsonpath.jsonpath(res_dict, "$.data")
        dataStr="".join(map(str,data))
        assert Work_DetailsDatas["data"] == dataStr



    def test_AllData(self):
        LoggerUtil().create_log().info("开始运行工单数据统计测试用例：{}".format(Work_DetailsDatas["AllData"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Work_DetailsDatas["api_AllData"], headers=headers)
        res_dict = json.loads((res.text))
        allPlan = jsonpath.jsonpath(res_dict, "$.data.allPlan")
        strAllPlan="".join(map(str,allPlan))
        intAllPlan=int(strAllPlan)
        assert Work_DetailsDatas["allPlan"] == intAllPlan




    def test_list(self):
        LoggerUtil().create_log().info("开始运行运维列表及服务评价测试用例：{}".format(Work_DetailsDatas["list"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Work_DetailsDatas["api_list"], json=json.dumps(Work_DetailsDatas["paload"]),headers=headers)
        res_dict = json.loads((res.text))
        pages = jsonpath.jsonpath(res_dict, "$.data.pages")
        pagesStr="".join(map(str,pages))
        intpages=int(pagesStr)
        assert Work_DetailsDatas["allPlan"] == intpages