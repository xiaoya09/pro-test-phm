import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml


Alarm_Path=os.path.join(configYaml+r'\ServiceDatas\Equipment_pages_api\FauitAlarm\Alarm.yaml')
Alarm_PathDatas=Yaml_data().read_yaml(Alarm_Path)


@allure.feature('报警故障列表')
class Test_Alarm:

    @allure.story("未读数量汇总")
    @allure.severity("normal")
    def test_getRecordCount(self):
        allure.dynamic.title("测试用例标题：%s" % (Alarm_PathDatas["getRecordCount"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Alarm_PathDatas["api_getRecordCount"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_getRecordCount"],data=Alarm_PathDatas["pload"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出processStatus字段"):
            processStatus = jsonpath.jsonpath(res_dict, "$.data.alarmRecordReadList[*].processStatus")
        with allure.step("第四步：将取出来的processStatus字段与预期做断言"):
            assert Alarm_PathDatas["processStatus"] in processStatus





    @allure.story("未通报")
    @allure.severity("normal")
    def test_info(self):
        allure.dynamic.title("测试用例标题：%s" % (Alarm_PathDatas["info"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Alarm_PathDatas["api_info"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info"],json=json.dumps(Alarm_PathDatas["pload"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出providerId字段"):
            providerId=jsonpath.jsonpath(res_dict,"$.data.records[*].providerId")
        with allure.step("第四步：将取出来的providerId字段与预期做断言"):
            assert Alarm_PathDatas["providerId"] in providerId
        with allure.step("第五步：取出列表第一个报警数据，然后返回出来，给handleProcessStatus接口做参数"):
            NoAlarm = jsonpath.jsonpath(res_dict, "$.data.records[0]")
            return NoAlarm[0]




    @allure.story("处理报警状态")
    @allure.severity("normal")
    def test_handleProcessStatus(self):
        allure.dynamic.title("测试用例标题：%s" % (Alarm_PathDatas["handleProcessStatus"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：从未通报的报警接口返回的数据，取一条报警数据，且将里面的reportButton的状态改为2"):
            jsonDatas = self.test_info()
            jsonDatas["reportButton"]=2
        with allure.step("第二步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Alarm_PathDatas["api_handleProcessStatus"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_handleProcessStatus"],json=json.dumps(jsonDatas),headers=headers)
        with allure.step("第三步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第四步：取出data字段，并转化为int"):
            datas = jsonpath.jsonpath(res_dict, "$.data")
            strdatas="".join(map(str,datas))
            intDatas=int(strdatas)
        with allure.step("第五步：将取出来的data与预期结果做断言"):
            assert Alarm_PathDatas["data"] == intDatas



    @allure.story("已通报")
    @allure.severity("normal")
    def test_info01(self):
        allure.dynamic.title("测试用例标题：%s" % (Alarm_PathDatas["info01"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Alarm_PathDatas["api_info01"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info01"],json=json.dumps(Alarm_PathDatas["pload_datas"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出size字段，并转化为int"):
            size=jsonpath.jsonpath(res_dict,"$.data.size")
            strsize = "".join(map(str, size))
            intsize = int(strsize)
        with allure.step("第四步：将取出来的size字段与预期做断言"):
            assert Alarm_PathDatas["size"] == intsize





    @allure.story("已忽略")
    @allure.severity("normal")
    def test_info02(self):
        allure.dynamic.title("测试用例标题：%s" % (Alarm_PathDatas["info02"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Alarm_PathDatas["api_info02"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info02"],json=json.dumps(Alarm_PathDatas["pload_datas01"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出size字段，并转化为int"):
            size01=jsonpath.jsonpath(res_dict,"$.data.size")
            strsize = "".join(map(str, size01))
            intsize = int(strsize)
        with allure.step("第四步：将取出来的size字段与预期做断言"):
            assert Alarm_PathDatas["size01"] == intsize




    @allure.story("已恢复")
    @allure.severity("normal")
    def test_info03(self):
        allure.dynamic.title("测试用例标题：%s" % (Alarm_PathDatas["info02"]))
        headers = {"Content-Type": "application/json", "Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Alarm_PathDatas["api_info03"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Alarm_PathDatas["api_info03"],
            json=json.dumps(Alarm_PathDatas["pload_datas02"]), headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出size字段，并转化为int"):
            size01 = jsonpath.jsonpath(res_dict, "$.data.size")
            strsize = "".join(map(str, size01))
            intsize = int(strsize)
        with allure.step("第四步：将取出来的size字段与预期做断言"):
            assert Alarm_PathDatas["size02"] == intsize





if __name__ == '__main__':
    ll=Test_Alarm().test_handleProcessStatus