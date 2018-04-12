# -*-coding: utf-8 -*-
from pay import get_pay_apis
from utils import generate_out_trade_no, generate_out_refund_no

def run():

    # 生成订单号
    out_trade_no = generate_out_trade_no()
    print(out_trade_no)

    apis = get_pay_apis('meituan', merchant_id='168236281')

    # print(apis.micropay.create(out_trade_no, '134591548881750246', 5, '美团支付测试', wxSubAppId='wx8da96b886ac21461'))
    # print('111111111111111')

    print(apis.order.query('20180412170043604154705995793769'))
    # print('22222222222222222')

    # print(apis.order.cancel('20180412160856084415938502084418'))
    # print('3333333333333333333333')

    # 生成退款单号
    out_refund_no = generate_out_refund_no()
    # print(apis.refund.apply('20180412164518195224170771599145', '20180412164922625205528248990168', 3, '退款测试'))
    # print(apis.refund.query('20180412164518195224170771599145', '20180412164922625205528248990167'))
    

    


run()