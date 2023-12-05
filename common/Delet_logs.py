import os

#清理日志工作
class DeletLog:
    def __init__(self,path):
        #path指的是文件路径
        self.path=path


    def delet_file(self):
        for path in [self.path]:

            #获取for循环中路径下的日志文件，以列表形式打开
            all_files=os.listdir(path)
            #排序处理
            all_files.sort()
            for num in range(len(all_files)):
                #删除日志文件
                os.remove(os.path.join(path,all_files[num]))


if __name__ == '__main__':
    ll=DeletLog("D:\pythonProject\pro-test-phm\logs")
    ll.delet_file()
