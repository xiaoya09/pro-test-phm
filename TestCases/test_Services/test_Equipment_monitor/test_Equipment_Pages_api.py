import os,jsonpath,json, allure
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Loggoing import LoggerUtil
from common.Path_Send import configYaml
from common.SendRequests import Request
from TestCases.conftest import read_token_yaml


Equipment_pages_api_Path=os.path.join(configYaml+r'\ServiceDatas\Equipment_pages_api\Equipment.yaml')
Equipment_pages_api_PathDatas=Yaml_data().read_yaml(Equipment_pages_api_Path)
"""
此测试类下的测试用例为大账号登录切换服务商进入设备监测页面的访问接口

"""

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
        print(paload_pointId)
        strpaload_pointId="".join(map(str,paload_pointId))
        intpaload_pointId=int(strpaload_pointId)
        assert Equipment_pages_api_PathDatas["pointId"] == intpaload_pointId





# if __name__ == '__main__':
#
#     ll=Test_isEquipment()
#     ll.test_detailPoint()
# # pytest test_Equipment_Pages_api.py -sq -m=isEquipment   运行只带打标记的测试用例
# #
# if __name__ == '__main__':
#     pytest.main(["test_Equipment_Pages_api.py","-s","--alluredir",r"..\Outputs\reports\tmp"])
