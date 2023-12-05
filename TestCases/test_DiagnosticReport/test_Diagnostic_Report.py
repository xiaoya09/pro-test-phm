import os,json,jsonpath

import pytest

from common.SendRequests import Request
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from TestCases.conftest import read_token_yaml


DiagnosticReportPath=os.path.join(configYaml+'\DiagnosticReport.yaml')
DiagnosticReportDatas=Yaml_data().read_yaml(DiagnosticReportPath)

class Test_Report:

    def test_DiagnosticReport(self):
        LoggerUtil().create_log().info("开始运行首页---待处理报告列表-list：{}".format(DiagnosticReportDatas["list"]))
        headers={
            "Content-Type":"application/json",
            "Authorization":read_token_yaml()}
        res = Request().post_json_requests(conf.get("set", "test_url") +DiagnosticReportDatas["api_list"],json=json.dumps(DiagnosticReportDatas["paload"]), headers=headers)
        res_dict=json.loads((res.text))
        enterpriseName=jsonpath.jsonpath(res_dict,"$..records[*].enterpriseName")
        #判断预期的企业名称是否在返回的列表里
        assert DiagnosticReportDatas["enterpriseName"] in enterpriseName



    def test_statisticsFutureReport(self):
        LoggerUtil().create_log().info("开始运行首页---未来一月统计待处理报告：{}".format(DiagnosticReportDatas["statisticsFutureReport"]))
        headers={
            "Content-Type":"application/json",
            "Authorization":read_token_yaml()}
        res = Request().post_json_requests(conf.get("set", "test_url") +DiagnosticReportDatas["api_statisticsFutureReport"], headers=headers)
        res_dict=json.loads((res.text))
        num=jsonpath.jsonpath(res_dict,"$..data[*].num")
        assert DiagnosticReportDatas["num"] in num



    def test_optionselect(self):
        LoggerUtil().create_log().info("开始运行企业名称下拉选择测试用例：{}".format(DiagnosticReportDatas["optionselect"]))
        headers={
            "Content-Type":"application/json",
            "Authorization":read_token_yaml()}
        res = Request().get_requests(conf.get("set", "test_url") +DiagnosticReportDatas["api_optionselect"], headers=headers)
        res_dict=json.loads((res.text))
        enterpriseId=jsonpath.jsonpath(res_dict,"$..data[*].enterpriseId")
        assert DiagnosticReportDatas["enterpriseId"] in enterpriseId




    def test_list(self):
        LoggerUtil().create_log().info("开始运行报告规则设置列表测试用例：{}".format(DiagnosticReportDatas["rule_list"]))
        headers={
            "Content-Type":"application/json",
            "Authorization":read_token_yaml()}
        res = Request().post_json_requests(conf.get("set", "test_url") +DiagnosticReportDatas["api_rule_list"],json=json.dumps(DiagnosticReportDatas["paload_rule"]), headers=headers)
        res_dict=json.loads((res.text))
        record_enterpriseName=jsonpath.jsonpath(res_dict,"$..records[*].enterpriseName")
        assert DiagnosticReportDatas["record_enterpriseName"] in record_enterpriseName




    def test_addOrUpdateReportRule(self):
        LoggerUtil().create_log().info("开始运行设置报告规则测试用例：{}".format(DiagnosticReportDatas["addOrUpdateReportRule"]))
        headers={
            "Content-Type":"application/json",
            "Authorization":read_token_yaml()}
        res = Request().post_json_requests(conf.get("set", "test_url") +DiagnosticReportDatas["api_addOrUpdateReportRule"],json=json.dumps(DiagnosticReportDatas["paload_add"]), headers=headers)
        res_dict=json.loads((res.text))
        data=jsonpath.jsonpath(res_dict,"$.data")
        #返回的data数据是列表，将列表转换为字符串之后再转化为布尔类型
        dataStr="".join(map(str, data))
        boolean=bool(dataStr)
        assert DiagnosticReportDatas["data"] == boolean








if __name__ == '__main__':
    pytest.main([""])