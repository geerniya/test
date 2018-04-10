# -*-coding: utf-8 -*-
from pay import get_pay_apis

def run():
    apis = get_pay_apis('meituan', merchant_id='168236281')
    apis.micropay.create(None, '123423432452342', 2, '美团支付测试', wxSubAppId='wx8da96b886ac21461')

