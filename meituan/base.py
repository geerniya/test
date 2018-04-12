# -*- coding: utf-8 -*-

class BaseAPI(object):
    def __init__(self, client):
        self._client = client

    def _post(self, api_endpoint, **kwargs):
        return self._client.post(api_endpoint, **kwargs)