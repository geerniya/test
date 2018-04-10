# -*-coding: utf-8 -*-
import copy
from micropay import MeituanMicropay

MEITUAN = {
    'appid': '31161',
    'appsecret': 'ddf5cc4e5b504343aef4c406bf8fbd8f',
}


def get_pay_apis(api_type, **kwargs):
    if api_type = 'meituan':
        appid = MEITUAN['appid']
        appsecret = MEITUAN['appsecret']
        merchant_id = kwargs['merchant_id']
        return MeituanPay(appid, appsecret, merchant_id)

    elif api_type == 'alibaba':
        pass


class MeituanPay(object):
    API_BASE_URL = "https://openpay.meituan.com/"

    def __init__(self, appid, appsecret, merchant_id):
        self.appid = appid
        self.appsecret = appsecret
        self.merchant_id = merchant_id

        self.micorpay = MeituanMicropay(self)

    def _request(method, api_endpoint, **kwargs):
        url = '{0}{1}'.format(API_BASE_URL, api_endpoint)
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
        params['random'], params['sign'] = randon_string, sign






    def post(self, api_endpoint, **kwargs):
        return self._request(
            method='post',
            api_endpoint,
            **kwargs
        )
