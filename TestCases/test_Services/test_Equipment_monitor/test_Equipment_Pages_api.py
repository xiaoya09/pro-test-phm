import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml


Equipment_pages_api_Path=os.path.join(configYaml+r'\ServiceDatas\Equipment_pages_api\Equipment.yaml')
Equipment_pages_api_PathDatas=Yaml_data().read_yaml(Equipment_pages_api_Path)

@allure.title('设备监测页面的访问接口')
class Test_isEquipment:

    @allure.feature("设备是否装置测试用例")
    def test_isEquipment(self):
        LoggerUtil().create_log().info("开始运行设备是否装置测试用例：{}".format(Equipment_pages_api_PathDatas["isEquipment"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_isEquipment"],headers=headers)
        res_dict = json.loads((res.text))
        equipment = jsonpath.jsonpath(res_dict, "$.data.equipment")
        strEquipment="".join(map(str,equipment))
        boolE=bool(strEquipment)
        assert Equipment_pages_api_PathDatas["equipment"] == boolE






    def test_detail(self):
        LoggerUtil().create_log().info("开始运行查看部位信息:测点，过滤波形测试用例：{}".format(Equipment_pages_api_PathDatas["detail"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_detail"],data=Equipment_pages_api_PathDatas["paload"],headers=headers)
        res_dict = json.loads((res.text))
        bw_id = jsonpath.jsonpath(res_dict, "$.data.id")
        strEquipment="".join(map(str,bw_id))
        intbw_id=int(strEquipment)
        assert Equipment_pages_api_PathDatas["bw_id"] == intbw_id



    def test_detailByTren(self):
        LoggerUtil().create_log().info("开始运行查看部位信息-趋势预警测试用例：{}".format(Equipment_pages_api_PathDatas["detailByTren"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_detailByTren"],data=Equipment_pages_api_PathDatas["paload_bw"],headers=headers)
        res_dict = json.loads((res.text))
        terend_bw_id = jsonpath.jsonpath(res_dict, "$.data.id")
        strterend_bw_id="".join(map(str,terend_bw_id))
        intterend_bw_id=int(strterend_bw_id)
        assert Equipment_pages_api_PathDatas["terend_bw_id"] == intterend_bw_id




    def test_detailPoint(self):
        LoggerUtil().create_log().info("开始运行查看测点详情测试用例：{}".format(Equipment_pages_api_PathDatas["detailPoint"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_detailPoint"],data=Equipment_pages_api_PathDatas["paload_pointId"],headers=headers)
        res_dict = json.loads((res.text))
        paload_pointId = jsonpath.jsonpath(res_dict, "$.data.id")
        strpaload_pointId="".join(map(str,paload_pointId))
        intpaload_pointId=int(strpaload_pointId)
        assert Equipment_pages_api_PathDatas["pointId"] == intpaload_pointId



    def test_device_base_host_type(self):
        LoggerUtil().create_log().info("开始运行查看查看设备类型测试用例：{}".format(Equipment_pages_api_PathDatas["device_base_host_type"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_device_base_host_type"],headers=headers)
        res_dict = json.loads((res.text))
        createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        assert Equipment_pages_api_PathDatas["createBy"] in createBy




    def test_device_base_flexibility(self):
        LoggerUtil().create_log().info("开始运行查看设备基础信息测试用例：{}".format(Equipment_pages_api_PathDatas["device_base_flexibility"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_device_base_flexibility"],headers=headers)
        res_dict = json.loads((res.text))
        createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        assert Equipment_pages_api_PathDatas["createBy_device"] in createBy




    def test_nodeDeviceListDataAuth(self):
        LoggerUtil().create_log().info("开始运行查看设备洞察节点列表测试用例：{}".format(Equipment_pages_api_PathDatas["nodeDeviceListDataAuth"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_nodeDeviceListDataAuth"],headers=headers)
        res_dict = json.loads((res.text))
        nodeName = jsonpath.jsonpath(res_dict, "$.data[*].nodeName")
        assert Equipment_pages_api_PathDatas["nodeName"] in nodeName





    def test_main(self):
        LoggerUtil().create_log().info("开始运行设备详情（机器大脑）测试用例：{}".format(Equipment_pages_api_PathDatas["main"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_main"],headers=headers)
        res_dict = json.loads((res.text))
        createBy = jsonpath.jsonpath(res_dict, "$.data.createBy")
        assert Equipment_pages_api_PathDatas["createBy_main"] in createBy






    def test_healthCondition(self):
        LoggerUtil().create_log().info("开始运行设备健康分数测试用例：{}".format(Equipment_pages_api_PathDatas["healthCondition"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_healthCondition"],headers=headers)
        res_dict = json.loads((res.text))
        deviceId = jsonpath.jsonpath(res_dict, "$.data.deviceId")
        strdeviceid = "".join(map(str, deviceId))
        intdeviceid = int(strdeviceid)
        assert Equipment_pages_api_PathDatas["deviceId"] == intdeviceid




    def test_queryPointByDeviceId(self):
        LoggerUtil().create_log().info("开始运行设备测点，查询有测点的部位测试用例：{}".format(Equipment_pages_api_PathDatas["queryPointByDeviceId"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_queryPointByDeviceId"],data=Equipment_pages_api_PathDatas["paload_pointd"],headers=headers)
        res_dict = json.loads((res.text))
        createBy = jsonpath.jsonpath(res_dict, "$.data[*].createBy")
        assert Equipment_pages_api_PathDatas["createBy_name"] in createBy




    def test_img(self):
        LoggerUtil().create_log().info("开始运行查询设备图片-img测试用例：{}".format(Equipment_pages_api_PathDatas["img"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_img"],headers=headers)
        res_dict = json.loads((res.text))
        deviceId = jsonpath.jsonpath(res_dict, "$.data.deviceId")
        strdeviceid = "".join(map(str, deviceId))
        intdeviceid = int(strdeviceid)
        assert Equipment_pages_api_PathDatas["deviceId_01"] == intdeviceid





    def test_operationRate(self):
        LoggerUtil().create_log().info("开始运行设备开机率测试用例：{}".format(Equipment_pages_api_PathDatas["operationRate"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_operationRate"],data=Equipment_pages_api_PathDatas["data"],headers=headers)
        res_dict = json.loads((res.text))
        msg = jsonpath.jsonpath(res_dict, "$.msg")
        strmsg = "".join(map(str, msg))
        assert Equipment_pages_api_PathDatas["msg"] == strmsg






    def test_getAlarmDate(self):
        LoggerUtil().create_log().info("开始运行设备洞察趋势图，高低报时间测试用例：{}".format(Equipment_pages_api_PathDatas["getAlarmDate"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_getAlarmDate"],headers=headers)
        res_dict = json.loads((res.text))
        alarmStatus = jsonpath.jsonpath(res_dict, "$.data[*].alarmStatus")
        assert Equipment_pages_api_PathDatas["alarmStatus"] in alarmStatus








    def test_info(self):
        LoggerUtil().create_log().info("开始运行报警分页展示测试用例：{}".format(Equipment_pages_api_PathDatas["info"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_info"],json=json.dumps(Equipment_pages_api_PathDatas["paload_json"]),headers=headers)
        res_dict = json.loads((res.text))
        enterpriseName = jsonpath.jsonpath(res_dict, "$.data.records[*].enterpriseName")
        assert Equipment_pages_api_PathDatas["enterpriseName01"] in enterpriseName





    def test_health(self):
        LoggerUtil().create_log().info("开始运行设备健康评分测试用例：{}".format(Equipment_pages_api_PathDatas["health"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().get_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_health"],headers=headers)
        res_dict = json.loads((res.text))
        deviceId = jsonpath.jsonpath(res_dict, "$.data.deviceId")
        assert Equipment_pages_api_PathDatas["deviceId02"] in deviceId




    def test_getDevicePointTimeS(self):
        LoggerUtil().create_log().info("开始运行默认显示设备测点时间段趋势图带报警数据测试用例：{}".format(Equipment_pages_api_PathDatas["getDevicePointTimeSlotAndAlarmDefault"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_getDevicePointTimeSlotAndAlarmDefault"],data=Equipment_pages_api_PathDatas["pload_device"],headers=headers)
        res_dict = json.loads((res.text))
        iotId = jsonpath.jsonpath(res_dict, "$.data.iotId")
        assert Equipment_pages_api_PathDatas["iotId"] in iotId




    def test_add(self):
        LoggerUtil().create_log().info("开始运行添加诊断结论测试用例：{}".format(Equipment_pages_api_PathDatas["add"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_add"],json=json.dumps(Equipment_pages_api_PathDatas["paload_id"]),headers=headers)
        res_dict = json.loads((res.text))
        datas = jsonpath.jsonpath(res_dict, "$.data")
        strdatas="".join(map(str,datas))
        assert Equipment_pages_api_PathDatas["datas"] in strdatas





    def test_pointTrend(self):
        LoggerUtil().create_log().info("开始运行装置趋势图测试用例：{}".format(Equipment_pages_api_PathDatas["pointTrend"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_pointTrend"],json=json.dumps(Equipment_pages_api_PathDatas["paload_devices"]),headers=headers)
        res_dict = json.loads((res.text))
        unit = jsonpath.jsonpath(res_dict, "$.data.unit")
        assert Equipment_pages_api_PathDatas["unit"] in unit




    def test_signature(self):
        LoggerUtil().create_log().info("开始运行获取数据中台请求签名测试用例：{}".format(Equipment_pages_api_PathDatas["signature"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_signature"],headers=headers)
        res_dict = json.loads((res.text))
        msg = jsonpath.jsonpath(res_dict, "$.msg")
        Strmsg="".join(map(str,msg))
        assert Equipment_pages_api_PathDatas["msg01"] == Strmsg




    def test_getPointCustom(self):
        LoggerUtil().create_log().info("开始运行回显自定义测点测试用例：{}".format(Equipment_pages_api_PathDatas["getPointCustom"]))
        headers = {"Authorization": read_token_yaml()}
        res = Request().post_form_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_getPointCustom"],data=Equipment_pages_api_PathDatas["paload_device01"],headers=headers)
        res_dict = json.loads((res.text))
        id = jsonpath.jsonpath(res_dict, "$.data.id")
        Strid="".join(map(str,id))
        assert Equipment_pages_api_PathDatas["id"] == Strid






    def test_edit(self):
        LoggerUtil().create_log().info("开始运行编辑图片打点测试用例：{}".format(Equipment_pages_api_PathDatas["edit"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().put_requests(
            Equipment_pages_api_PathDatas["url"] ,json=json.dumps(Equipment_pages_api_PathDatas["paload_device02"]),headers=headers)
        res_dict = json.loads((res.text))
        data = jsonpath.jsonpath(res_dict, "$.data")
        Strdata="".join(map(str,data))
        assert Equipment_pages_api_PathDatas["data2"] == Strdata





    def test_addPointCustom(self):
        LoggerUtil().create_log().info("开始运行新增或编辑自定义测点测试用例：{}".format(Equipment_pages_api_PathDatas["addPointCustom"]))
        headers = {"Content-Type":"application/json","Authorization": read_token_yaml()}
        res = Request().post_json_requests(
            conf.get("set", "test_url") + Equipment_pages_api_PathDatas["api_addPointCustom"],json=json.dumps(Equipment_pages_api_PathDatas["paload_device03"]),headers=headers)
        res_dict = json.loads((res.text))
        data = jsonpath.jsonpath(res_dict, "$.data")
        Strdata="".join(map(str,data))
        assert Equipment_pages_api_PathDatas["data3"] == Strdata


















# if __name__ == '__main__':
#
#     ll=Test_isEquipment()
#     ll.test_detailPoint()
# # pytest test_Equipment_Pages_api.py -sq -m=isEquipment   运行只带打标记的测试用例
# #
# if __name__ == '__main__':
#     pytest.main(["test_Equipment_Pages_api.py","-s","--alluredir",r"..\Outputs\Outputs\tmp"])
