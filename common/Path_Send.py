import os

#获取当前commonPath的路径
daseDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#测试用例路径
TestCase=os.path.join(daseDir,r"TestCases\Test_Login\test_login.py")



#测试报告路径
Outputs=os.path.join(daseDir,r"reports\tmp")

#日志路径
Outputslog=os.path.join(daseDir,"logs")


#配置文件路径
configpath=os.path.join(daseDir,"config\config_profile.ini")

#配置yaml文件路径
configYaml=os.path.join(daseDir,"Datas")





