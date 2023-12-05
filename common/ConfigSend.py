import os
from configparser import ConfigParser
from common.Path_Send import configpath

#将配置的文件封装起来，便于其它函数调用直接读取数据
class Configsend(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")

file_path=os.path.join(configpath)
conf=Configsend(file_path)
print(conf.get("log","name"))


if __name__ == '__main__':
    ll=Configsend()