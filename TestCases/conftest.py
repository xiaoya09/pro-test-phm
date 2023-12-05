import pytest
from common.YamlData import Yaml_data
from common.GetToken import GetToken


@pytest.fixture(scope='session')
def cleal_Datas():
    """
    登录前先清理之前测试用例产生的日志数据，再清理之前保存token的yaml文件，然后重新生成新的token
    :return:
    """
    from common.ConfigSend import conf
    from common.Delet_logs import DeletLog
    #先清理日志文件
    delete_files=DeletLog("D:\pythonProject\pro-test-phm\logs")
    delete_files.delet_file()

    #删除Token.yaml中之前保存的token数据
    tokenYaml=Yaml_data().read_yaml(conf.get('set',"TokenYaml"))
    del tokenYaml["phm"]

    #获取新的token并写入到Token.yaml中
    token=GetToken().test_token()
    Yaml_data().write_yaml(conf.get('set',"TokenYaml"), {"phm": token})



def read_token_yaml():
    from common.ConfigSend import conf
    phmToken = Yaml_data().read_yaml(conf.get('set',"TokenYaml"))
    return phmToken["phm"]
