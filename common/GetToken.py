from common.SendRequests import Request

class GetToken:
    # 登录前获取uuid
    def test_uuid(self):
        url="https://web-pro-test.imotorlinx.cn/imotor-api/imotor/oauth/image/captcha"
        res = Request().get_requests(url)
        res_dict = res.json()
        self.uuid = res_dict['data']['uuid']
        return self.uuid


   #获取token
    def test_token(self):
        url="https://web-pro-test.imotorlinx.cn/imotor-api/imotor/oauth/token"
        header={'Content-Type': 'application/x-www-form-urlencoded'}
        payload ={'client_id': 'imotor', 'client_secret': 123, 'platform': 'imotor-member', 'username': 'admin', 'password': '3iSllmCPeWWy/fRMOmKb4e1mfuI8Bhb/ekmf5n/c2C06Xs2IEL6r6X3JqvDFDvid+XGRDqrvtYCVcZQRoFgMQA==', 'code': 'V587', 'uuid': '305e8778ee464829ac8fb1d06410a673', 'grant_type': 'password'}
        res = Request().post_form_requests(url, data=payload,
                                           headers=header)
        res_dict = res.json()
        self.access_token = res_dict["data"]["access_token"]
        return self.access_token
        # Yaml_data().write_yaml(os.path.join(daseDir,"token.yaml"),{"phm": self.access_token})



if __name__ == '__main__':
    ll=GetToken().test_token()
    print(ll)
