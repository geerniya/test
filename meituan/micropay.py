# -*- coding: utf-8 -*-

from base import BaseAPI
from utils import generate_out_trade_no
from exceptions import InvalidAuthCode

class MeituanMicropay(BaseAPI):
    """
    创建订单需要的参数：

    channel	  	 支付渠道
    outTradeNo	 接入方订单号 不超过64位
    authCode	 用户付款码
    totalFee	 总金额, 以分为单位
    subject	     商品标题
    body	     商品详情
    expireMinutes    创建支付订单后，订单关闭时间，单位为分钟。默认设置为5分钟,最长不超过30分钟，超过关单时间无法支付
    merchantId	 开放平台分配的商户id, 目前是 美团POI ID
    appId	     接入方标识，由美团开放平台分配 参考 https://platform.meituan.com/buffet/list
    sign	     验证签名
    random	     随机数
    """

    def create(self, out_trade_no, auth_code, total_fee, subject, **kwargs):
        # 生成订单编号
        if not out_trade_no:
            out_trade_no = generate_out_trade_no()

        # 通过用户付款码auth_code前两位判断用户支付类型，是支付宝支付还是微信支付
        # 前两位为10、11、12、13、14、15，则为微信支付
        # 前两位为25、26、27、28、29、30，则为支付宝支付
        channel = None
        if len(auth_code) == 18 and str(auth_code)[:2] in ['10', '11', '12', '13', '14', '15']:
            channel = 'wx_barcode_pay'
        elif 16 <= len(auth_code) <= 24 and str(auth_code)[:2] in ['25', '26', '27', '28', '29', '30']:
            channel = 'ali_barcode_pay'
        if channel == None:
            raise InvalidAuthCode(auth_code)
        
        params = {
            'outTradeNo': out_trade_no, 
            'authCode': auth_code, 
            'totalFee': total_fee,
            'subject': subject,
            'body': kwargs['body'] if kwargs.get('body') else subject,
            'channel': channel,
            'expireMinutes':  kwargs['expireMinutes'] if kwargs.get('expireMinutesbody') else 3,

        }
    
        return self._post('api/pay/micropay', params=params)





        




