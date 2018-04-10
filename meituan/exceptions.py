# -*- coding: utf-8 -*-

class InvalidAuthCode(Exception):
    def __init__(self, auth_code):
        super().__init__(auth_code)