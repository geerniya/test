# -*- coding: utf-8 -*-
from base import BaseAPI

class MeituanRefundAPI(BaseAPI):
    def apply(self, out_trade_no, out_refund_no, refund_fee, reason):
        params = {
            'outTradeNo': out_trade_no, 
            'refundNo': out_refund_no,
            'refundFee': refund_fee,
            'refundReason': reason
        }

        return self._post('api/refund', params=params)
    

    def query(self, out_trade_no, out_refund_no):
        params = {
            'outTradeNo': out_trade_no, 
            'refundNo': out_refund_no,
        }

        return self._post('api/refund/query', params=params)