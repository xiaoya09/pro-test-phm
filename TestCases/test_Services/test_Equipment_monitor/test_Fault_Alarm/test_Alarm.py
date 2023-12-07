import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml


Alarm_Path=os.path.join(configYaml+r'\ServiceDatas\Equipment_pages_api\FauitAlarm\Alarm.yaml')
Alarm_PathDatas=Yaml_data().read_yaml(Alarm_Path)
"""
此测试类下的测试用例为大账号登录切换服务商进入设备监测--故障报警列表页

"""

@allure.title('报警故障列表')
class Test_Alarm:

    @allure.feature("获取未读数量汇总")
    def test_getRecordCount(self):
        LoggerUtil().create_log().info("开始运行未读数量汇总测试用例：{}".format(Alarm_PathDatas["getRecordCount"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_getRecordCount"],data=Alarm_PathDatas["pload"],headers=headers)
        res_dict = json.loads((res.text))
        processStatus = jsonpath.jsonpath(res_dict, "$.data.alarmRecordReadList[*].processStatus")
        assert Alarm_PathDatas["processStatus"] in processStatus



    def test_info(self):
        LoggerUtil().create_log().info("开始运行未通报测试用例：{}".format(Alarm_PathDatas["info"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info"],json=json.dumps(Alarm_PathDatas["pload"]),headers=headers)
        res_dict = json.loads((res.text))
        providerId=jsonpath.jsonpath(res_dict,"$.data.records[*].providerId")
        assert Alarm_PathDatas["providerId"] in providerId
        NoAlarm = jsonpath.jsonpath(res_dict, "$.data.records[0]")
        return NoAlarm[0]




    def test_handleProcessStatus(self):
        LoggerUtil().create_log().info("开始运行处理报警状态测试用例：{}".format(Alarm_PathDatas["handleProcessStatus"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        #从未通报的报警接口返回的数据，取一条报警数据，且将里面的reportButton的状态改为2
        jsonDatas = self.test_info()
        jsonDatas["reportButton"]=2
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_handleProcessStatus"],json=json.dumps(jsonDatas),headers=headers)
        res_dict = json.loads((res.text))
        datas = jsonpath.jsonpath(res_dict, "$.data")
        strdatas="".join(map(str,datas))
        intDatas=int(strdatas)
        assert Alarm_PathDatas["data"] == intDatas


    def test_info01(self):
        LoggerUtil().create_log().info("开始运行已通报测试用例：{}".format(Alarm_PathDatas["info01"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info01"],json=json.dumps(Alarm_PathDatas["pload_datas"]),headers=headers)
        res_dict = json.loads((res.text))
        size=jsonpath.jsonpath(res_dict,"$.data.size")
        strsize = "".join(map(str, size))
        intsize = int(strsize)
        assert Alarm_PathDatas["size"] == intsize




    def test_info02(self):
        LoggerUtil().create_log().info("开始运行已忽略测试用例：{}".format(Alarm_PathDatas["info02"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info02"],json=json.dumps(Alarm_PathDatas["pload_datas01"]),headers=headers)
        res_dict = json.loads((res.text))
        size01=jsonpath.jsonpath(res_dict,"$.data.size")
        strsize = "".join(map(str, size01))
        intsize = int(strsize)
        assert Alarm_PathDatas["size01"] == intsize





    def test_info03(self):
        LoggerUtil().create_log().info("开始运行已忽略测试用例：{}".format(Alarm_PathDatas["info02"]))
        headers = {"Content-Type": "application/json", "Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info03"],
            json=json.dumps(Alarm_PathDatas["pload_datas02"]), headers=headers)
        res_dict = json.loads((res.text))
        size01 = jsonpath.jsonpath(res_dict, "$.data.size")
        strsize = "".join(map(str, size01))
        intsize = int(strsize)
        assert Alarm_PathDatas["size02"] == intsize





if __name__ == '__main__':
    ll=Test_Alarm().test_handleProcessStatus