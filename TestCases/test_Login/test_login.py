import allure
import pytest,os
from common.SendRequests import Request
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml




@allure.feature("登录模块接口")
class Test_Login:

    #正常登录
    @allure.story("登录接口")
    @allure.severity("blocker")
    @pytest.mark.parametrize("cases",Yaml_data().read_yaml(os.path.join(configYaml,'login.yaml')))
    def test_login(self,cases):
        allure.dynamic.title("测试用例标题：%s" % (cases['title']))
        with allure.step("第一步：发送post请求，接口地址：{}".format(conf.get("set", "test_url") +cases['login_url'])):
            res = Request().post_form_requests(conf.get("set", "test_url") +cases['login_url'],data=cases["paload"], headers=cases["headers"])
        with allure.step("第二步：将接口返回的数据转化为json格式"):
            res_dict=res.json()
        with allure.step("第三步：将接口返回的msg字段与预期结果断言"):
            assert cases["msg"]==res_dict["msg"]



