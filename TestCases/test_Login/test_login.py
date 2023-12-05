import allure
import pytest,os
from common.SendRequests import Request
from common.YamlData import Yaml_data
from common.ConfigSend import conf
from common.Path_Send import configYaml



@allure.title("登录模块")
class Test_Login:

    #正常登录

    @pytest.mark.parametrize("cases",Yaml_data().read_yaml(os.path.join(configYaml,'login.yaml')))
    def test_login(self,cases):
        res = Request().post_form_requests(conf.get("set", "test_url") +cases['login_url'],data=cases["paload"], headers=cases["headers"])
        res_dict=res.json()
        assert cases["msg"]==res_dict["msg"]

if __name__ == '__main__':
    pytest.main(["-vs"])
