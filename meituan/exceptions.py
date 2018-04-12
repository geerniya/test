# -*- coding: utf-8 -*-

class InvalidAuthCode(Exception):
    def __init__(self, auth_code):
        errmsg = 'invalid authcode: {0}'.format(auth_code)
        super().__init__(errmsg)


class MeituanAPIException(Exception):
    def __init__(self, errCode, errMsg, subCode, subMsg):
        self.errCode = errCode,
        self.errMsg = errMsg,
        self.subCode = subCode,
        self.subMsg = subMsg
    
    def __str__(self):
        _str = "Error code: {errCode}, message: {errMsg}. Suberror code: {subCode}, Submessage: {subMsg}".format(
                errCode=self.errCode,
                errMsg=self.errMsg,
                subCode=self.subCode,
                subMsg=self.subMsg
            )

        return _str
