import requests
from common.Loggoing import LoggerUtil
#将不同的请求方式单独封装起来，便于调用

class Request:

    #get请求方式
    def get_requests(self,url,data=None,**kwargs):

        LoggerUtil().create_log().info("请求地址：{}".format(url))
        LoggerUtil().create_log().info("请求数据{}".format(data))
        self.respones=requests.get(url,data,**kwargs)
        LoggerUtil().create_log().info("响应数据{}".format(self.respones.text))
        return self.respones


    #post请求方式，传参格式要求是表单形式：application/x-www-form-urlencoded;charset=UTF-8
    def post_form_requests(self,url,data=None,**kwargs):

        LoggerUtil().create_log().info("请求地址：{}".format(url))
        LoggerUtil().create_log().info("请求数据{}".format(data))
        self.respones = requests.post(url, data,**kwargs)
        LoggerUtil().create_log().info("响应数据{}".format(self.respones.text))
        return self.respones



    #post请求方式，传参格式要求是json形式：application/json
    def post_json_requests(self,url,json=None,**kwargs):

        LoggerUtil().create_log().info("请求地址：{}".format(url))
        LoggerUtil().create_log().info("请求数据{}".format(json))
        self.respones = requests.post(url, json,**kwargs)
        LoggerUtil().create_log().info("响应数据{}".format(self.respones.text))
        return self.respones




    #put请求方式，传参格式要求是json形式：application/json
    def put_requests(self,url,json=None,**kwargs):

        LoggerUtil().create_log().info("请求地址：{}".format(url))
        LoggerUtil().create_log().info("请求数据{}".format(json))
        self.respones = requests.put(url, json,**kwargs)
        LoggerUtil().create_log().info("响应数据{}".format(self.respones.text))
        return self.respones





# if __name__ == '__main__':
#     # ree=send_requests()
#     # url = "https://web-pro-test.imotorlinx.cn/imotor-api/imotor/oauth/image/captcha"
#     #
#     # l=ree.get_requests(url)
#     # ditctt=l.json()
#     # uuid = ditctt['data']['uuid']
