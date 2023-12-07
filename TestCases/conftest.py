import pytest
from common.GetToken import GetToken
from common.Path_Send import TokenYamlPath
from common.YamlData import Yaml_data

@pytest.fixture(scope="session",autouse=True)
def get_token():
    #先清理token.yaml中之前存得token值
    Yaml_data().clear_yaml(TokenYamlPath)
    #获取新的toke值
    newToken=GetToken().test_token()
    #将新的值写入token.yaml
    Yaml_data().write_yaml(TokenYamlPath, {"phm":newToken })



def read_token_yaml():
    #读取新的token值
    readYaml=Yaml_data().read_yaml(TokenYamlPath)
    phmTkone=readYaml["phm"]
    return phmTkone

