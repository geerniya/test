# -*-coding: utf-8 -*-
from pay import get_pay_apis

def run():
    apis = get_pay_apis('meituan', merchant_id='168236281')
    print(apis.micropay.create(None, '134726959169143255', 1, '美团支付测试', wxSubAppId='wx8da96b886ac21461'))
    print('111111111111111')

run()