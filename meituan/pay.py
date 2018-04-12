# -*-coding: utf-8 -*-
import copy
import requests

from micropay import MeituanMicropay
from exceptions import InvalidAuthCode, MeituanAPIException
from utils import calculate_sign

MEITUAN = {
    'appid': '31161',
    'appsecret': 'ddf5cc4e5b504343aef4c406bf8fbd8f',
}


def get_pay_apis(api_type, **kwargs):
    if api_type == 'meituan':
        appid = MEITUAN['appid']
        appsecret = MEITUAN['appsecret']
        merchant_id = kwargs['merchant_id']
        return MeituanPay(appid, appsecret, merchant_id)

    elif api_type == 'alibaba':
        pass


class MeituanPay(object):
    API_BASE_URL = "https://openpay.meituan.com/"
    _http = requests.Session()

    def __init__(self, appid, appsecret, merchant_id):
        self.appid = appid
        self.appsecret = appsecret
        self.merchant_id = merchant_id

        self.micropay = MeituanMicropay(self)

    def _request(self, method, api_endpoint, **kwargs):
        url = '{0}{1}'.format(self.API_BASE_URL, api_endpoint)
        params = kwargs['params']
        params['appId'], params['merchantId'] = self.appid, self.merchant_id

        # 生成签名和随机数
        # 特殊处理wxSubAppId（该参数不加入签名）
        if api_endpoint == 'api/pay/micropay':
            _params = copy.copy(params)
            if _params.get('wxSubAppId'):
                del _params['wxSubAppId']
            random_string, sign = calculate_sign(self.appsecret, _params)
        else:
            random_string, sign = calculate_sign(self.appsecret, params)

        params['random'], params['sign'] = random_string, sign

        res = self._http.request(method=method, url=url, json=params)
        res.raise_for_status()

        
        
        # 处理返回结果
        return self.handle_result(res)

    def handle_result(self, res):
        try:
            res = res.json()
        except:
            raise InvalidAuthCode("Meituan payment result json parsing error")
        print(res)
        if res['status'] == 'FAIL':
            raise MeituanAPIException(
                errCode=res['errCode'],
                errMsg=res['errMsg'],
                subCode=res['subCode'],
                subMsg=res['subMsg']
            )

        return res

   

    def post(self, api_endpoint, **kwargs):
        return self._request(
            'post',
            api_endpoint,
            **kwargs
        )
