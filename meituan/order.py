# -*- coding: utf-8 -*-
from base import BaseAPI

class MeituanOrderAPI(BaseAPI):
    def query(self, out_trade_no):
        params = {
            'outTradeNo': out_trade_no
        }

        return self._post('api/pay/query', params=params)

    def cancel(self, out_trade_no):
        params = {
            'outTradeNo': out_trade_no
        }

        return self._post('api/cancel', params=params)