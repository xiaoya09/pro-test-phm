import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml


Equipment_pages_api_Path=os.path.join(configYaml+r'\ServiceDatas\Equipment_pages_api\Equipment.yaml')
Equipment_pages_api_PathDatas=Yaml_data().read_yaml(Equipment_pages_api_Path)

@allure.feature("设备监测模块")
class Test_isEquipment:

    @allure.story("设备是否装置测试用例")
    @allure.severity("normal")
    def test_isEquipment(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["isEquipment"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_isEquipment"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_isEquipment"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的equipment字段，并转化为字符串，再转布尔类型"):
            equipment = jsonpath.jsonpath(res_dict, "$.data.equipment")
            strEquipment="".join(map(str,equipment))
            boolE=bool(strEquipment)
        with allure.step("第四步：将取出来的equipment字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["equipment"] == boolE





    @allure.story("查看部位信息")
    @allure.severity("normal")
    def test_detail(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["detail"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_detail"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_detail"],data=Equipment_pages_api_PathDatas["paload"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的id字段，并转化为字符串，再转int类型"):
            bw_id = jsonpath.jsonpath(res_dict, "$.data.id")
            strEquipment="".join(map(str,bw_id))
            intbw_id=int(strEquipment)
        with allure.step("第四步：将取出来的id字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["bw_id"] == intbw_id






    @allure.story("查看部位信息-趋势预警")
    @allure.severity("normal")
    def test_detailByTren(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["detailByTren"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_detailByTren"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_detailByTren"],data=Equipment_pages_api_PathDatas["paload_bw"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的id字段，并转化为字符串，再转int类型"):
            terend_bw_id = jsonpath.jsonpath(res_dict, "$.data.id")
            strterend_bw_id="".join(map(str,terend_bw_id))
            intterend_bw_id=int(strterend_bw_id)
        with allure.step("第四步：将取出来的id字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["terend_bw_id"] == intterend_bw_id





    @allure.story("查看测点详情")
    @allure.severity("normal")
    def test_detailPoint(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["detailPoint"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_detailPoint"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_detailPoint"],data=Equipment_pages_api_PathDatas["paload_pointId"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的id字段，并转化为字符串，再转int类型"):
            paload_pointId = jsonpath.jsonpath(res_dict, "$.data.id")
            strpaload_pointId="".join(map(str,paload_pointId))
            intpaload_pointId=int(strpaload_pointId)
        with allure.step("第四步：将取出来的id字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["pointId"] == intpaload_pointId




    @allure.story("查看设备类型")
    @allure.severity("normal")
    def test_device_base_host_type(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["device_base_host_type"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_device_base_host_type"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_device_base_host_type"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的createBy"):
            createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        with allure.step("第四步：将取出来的createBy字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["createBy"] in createBy




    @allure.story("查看设备基础信息")
    @allure.severity("normal")
    def test_device_base_flexibility(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["device_base_flexibility"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_device_base_flexibility"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_device_base_flexibility"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的createBy"):
            createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        with allure.step("第四步：将取出来的createBy字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["createBy_device"] in createBy





    @allure.story("查看设备洞察节点列表")
    @allure.severity("normal")
    def test_nodeDeviceListDataAuth(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["nodeDeviceListDataAuth"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_nodeDeviceListDataAuth"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_nodeDeviceListDataAuth"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的nodeName"):
            nodeName = jsonpath.jsonpath(res_dict, "$.data[*].nodeName")
        with allure.step("第四步：将取出来的nodeName字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["nodeName"] in nodeName




    @allure.story("设备详情（机器大脑）")
    @allure.severity("normal")
    def test_main(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["main"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_main"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_main"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的createBy"):
            createBy = jsonpath.jsonpath(res_dict, "$.data.createBy")
        with allure.step("第四步：将取出来的createBy字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["createBy_main"] in createBy





    @allure.story("设备健康分数")
    @allure.severity("normal")
    def test_healthCondition(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["healthCondition"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_healthCondition"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_healthCondition"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的deviceId,并转化为int"):
            deviceId = jsonpath.jsonpath(res_dict, "$.data.deviceId")
            strdeviceid = "".join(map(str, deviceId))
            intdeviceid = int(strdeviceid)
        with allure.step("第四步：将取出来的deviceId字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["deviceId"] == intdeviceid





    @allure.story("设备测点，查询有测点的部位")
    @allure.severity("normal")
    def test_queryPointByDeviceId(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["queryPointByDeviceId"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_queryPointByDeviceId"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_queryPointByDeviceId"],data=Equipment_pages_api_PathDatas["paload_pointd"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的createBy"):
            createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        with allure.step("第四步：将取出来的createBy字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["createBy_name"] in createBy






    @allure.story("查询设备图片-img")
    @allure.severity("normal")
    def test_img(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["img"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_img"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_img"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取data里面的deviceId，并转化为Int"):
            deviceId = jsonpath.jsonpath(res_dict, "$.data.deviceId")
            strdeviceid = "".join(map(str, deviceId))
            intdeviceid = int(strdeviceid)
        with allure.step("第四步：将取出来的deviceId字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["deviceId_01"] == intdeviceid





    @allure.story("设备开机率")
    @allure.severity("normal")
    def test_operationRate(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["operationRate"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_operationRate"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_operationRate"],data=Equipment_pages_api_PathDatas["data"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出msg"):
            msg = jsonpath.jsonpath(res_dict, "$.msg")
            strmsg = "".join(map(str, msg))
        with allure.step("第四步：将取出来的msg字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["msg"] == strmsg





    @allure.story("设备洞察趋势图，高低报时间")
    @allure.severity("normal")
    def test_getAlarmDate(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["getAlarmDate"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_getAlarmDate"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_getAlarmDate"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出alarmStatus"):
            alarmStatus = jsonpath.jsonpath(res_dict, "$.data[*].alarmStatus")
        with allure.step("第四步：将取出来的alarmStatus字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["alarmStatus"] in alarmStatus





    @allure.story("报警分页展示")
    @allure.severity("normal")
    def test_info(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["info"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_info"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_info"],json=json.dumps(Equipment_pages_api_PathDatas["paload_json"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出enterpriseName"):
            enterpriseName = jsonpath.jsonpath(res_dict, "$.data.records[*].enterpriseName")
        with allure.step("第四步：将取出来的enterpriseName字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["enterpriseName01"] in enterpriseName




    @allure.story("设备健康评分")
    @allure.severity("normal")
    def test_health(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["health"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送get请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_health"])):
            res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_health"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出deviceId"):
            deviceId = jsonpath.jsonpath(res_dict, "$.data.deviceId")
        with allure.step("第四步：将取出来的deviceId字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["deviceId02"] in deviceId




    @allure.story("默认显示设备测点时间段趋势图带报警数据")
    @allure.severity("normal")
    def test_getDevicePointTimeS(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["getDevicePointTimeSlotAndAlarmDefault"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_getDevicePointTimeSlotAndAlarmDefault"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_getDevicePointTimeSlotAndAlarmDefault"],data=Equipment_pages_api_PathDatas["pload_device"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出iotId"):
            iotId = jsonpath.jsonpath(res_dict, "$.data.iotId")
        with allure.step("第四步：将取出来的iotId字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["iotId"] in iotId




    @allure.story("添加诊断结论")
    @allure.severity("normal")
    def test_add(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["add"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_add"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_add"],json=json.dumps(Equipment_pages_api_PathDatas["paload_id"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出data字段"):
            datas = jsonpath.jsonpath(res_dict, "$.data")
            strdatas="".join(map(str,datas))
        with allure.step("第四步：将取出来的data字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["datas"] in strdatas





    @allure.story("装置趋势图")
    @allure.severity("normal")
    def test_pointTrend(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["pointTrend"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_pointTrend"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_pointTrend"],json=json.dumps(Equipment_pages_api_PathDatas["paload_devices"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出unit字段"):
            unit = jsonpath.jsonpath(res_dict, "$.data.unit")
        with allure.step("第四步：将取出来的unit字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["unit"] in unit




    @allure.story("获取数据中台请求签名")
    @allure.severity("normal")
    def test_signature(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["signature"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_signature"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_signature"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出msg字段"):
            msg = jsonpath.jsonpath(res_dict, "$.msg")
            Strmsg="".join(map(str,msg))
        with allure.step("第四步：将取出来的msg字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["msg01"] == Strmsg




    @allure.story("回显自定义测点")
    @allure.severity("normal")
    def test_getPointCustom(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["getPointCustom"]))
        headers = {"Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_getPointCustom"])):
            res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_getPointCustom"],data=Equipment_pages_api_PathDatas["paload_device01"],headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出id字段"):
            id = jsonpath.jsonpath(res_dict, "$.data.id")
            Strid="".join(map(str,id))
        with allure.step("第四步：将取出来的id字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["id"] == Strid





    @allure.story("编辑图片打点")
    @allure.severity("normal")
    def test_edit(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["edit"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送put请求，接口地址：{}".format(Equipment_pages_api_PathDatas["url"])):
            res = Request().put_requests(
            Equipment_pages_api_PathDatas["url"] ,json=json.dumps(Equipment_pages_api_PathDatas["paload_device02"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出data字段"):
            data = jsonpath.jsonpath(res_dict, "$.data")
            Strdata="".join(map(str,data))
        with allure.step("第四步：将取出来的data字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["data2"] == Strdata




    @allure.story("新增或编辑自定义测点")
    @allure.severity("normal")
    def test_addPointCustom(self):
        allure.dynamic.title("测试用例标题：%s" % (Equipment_pages_api_PathDatas["addPointCustom"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +Equipment_pages_api_PathDatas["api_addPointCustom"])):
            res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_addPointCustom"],json=json.dumps(Equipment_pages_api_PathDatas["paload_device03"]),headers=headers)
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict = json.loads((res.text))
        with allure.step("第三步：取出data字段"):
            data = jsonpath.jsonpath(res_dict, "$.data")
            Strdata="".join(map(str,data))
        with allure.step("第四步：将取出来的data字段与预期做断言"):
            assert Equipment_pages_api_PathDatas["data3"] == Strdata





# if __name__ == '__main__':
#
#     ll=Test_isEquipment()
#     ll.test_detailPoint()
# # pytest test_Equipment_Pages_api.py -sq -m=isEquipment   运行只带打标记的测试用例
# #
# if __name__ == '__main__':
#     pytest.main(["test_Equipment_Pages_api.py","-s","--alluredir",r"..\Outputs\Outputs\tmp"])
