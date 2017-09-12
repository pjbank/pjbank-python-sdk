#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pjbanksdk.config import __apiurls__ as apiurls

class PJBankAPI(object):
    """docstring for PJBankAPI."""

    def __init__(self):
        self._url = apiurls.get("sandbox")
        self._credencial = None
        self._chave = None
        self.__metodos = ["GET", "POST", "PUT", "DELETE"]
        self.__endpointBase = None

    def configurar(self, credencial=None, chave=None, modo=None):
        if credencial:
            self._credencial = credencial
        if chave:
            self._chave = chave
        if modo:
            self._url = apiurls.get(modo)
    
    def get_credencial(self):
        return self._credencial
    
    def get_chave(self):
        return self._chave

    def get_modo(self):
        return self._url

    def get_headers(self, parameter_list):
        raise NotImplementedError

    def get_endpoint(self, credenciais=False, *args):
        if credenciais:
            args = [self._credencial]+args
        return "/".join([self.__endpointBase]+args)
    
    def _request(self, metodo, endpoint, headers, dados=None, params=None):
        url = "/".join([self._url, self.__endpointBase, endpoint])
        return requests.request(metodo, url, data=dados, headers=headers, params=params)

    def _get(self, endpoint, headers):
        return self._request("GET", endpoint, headers)
    
    def _post(self, endpoint, headers, dados):
        return self._request("POST", endpoint, headers, dados)
    
    def _put(self, endpoint, headers, dados):
        return self._request("PUT", endpoint, headers, dados)
    
    def _delete(self, endpoint, headers, dados=None):
        return self._request("DELETE", endpoint, headers, dados)

