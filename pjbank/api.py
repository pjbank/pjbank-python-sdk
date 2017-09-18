#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pjbank.config import __apiurls__ as apiurls

class PJBankAPI(object):
    """Classe representando a API PJBank. A chamada deve especificar """

    def __init__(self, credencial=None, chave=None, modo="sandbox"):
        self._modo = modo
        self._url = apiurls.get(self._modo)
        self._endpoint_base = ''
        self._credencial = credencial
        self._chave = chave
        self._chave_headers = "X-CHAVE-CONTA"
        self._content_type = "application/json" 

    @property
    def credencial(self):
        return self._credencial

    @credencial.setter
    def credencial(self, credencial):
        self._credencial = credencial

    @property
    def chave(self):
        return self._chave
    
    @chave.setter
    def chave(self, chave):
        self._chave = chave
    
    @property
    def modo(self):
        return self._modo

    @modo.setter
    def modo(self, modo):
        if modo not in apiurls:
            raise Exception("Modo inválido. Use 'live' ou 'sandbox'.")
        self._modo = modo
        self._url = apiurls.get(self._modo)

    @property
    def headers_chave(self):
        return {self._chave_headers: self.chave}
    
    @property
    def headers_content(self):
        return {"Content-Type": self._content_type}
    
    def _get_endpoint(self, recursos=None):
        base = [self._url, self._endpoint_base]
        if recursos:
            base.extend(recursos)
        url = '/'.join(base)
        return url

    def _request(self, metodo, endpoint, headers, dados=None, params=None):
        url = self._get_endpoint(endpoint)
        return requests.request(metodo, url, data=dados, headers=headers, params=params)

    def _get(self, endpoint, headers, params=None):
        return self._request("GET", endpoint, headers, params)

    def _post(self, endpoint, headers, dados, params=None):
        return self._request("POST", endpoint, headers, dados, params)

    def _put(self, endpoint, headers, dados, params=None):
        return self._request("PUT", endpoint, headers, dados, params)

    def _delete(self, endpoint, headers, dados=None, params=None):
        return self._request("DELETE", endpoint, headers, dados, params)

    def configurar(self, credencial=None, chave=None, modo=None):
        if credencial:
            self.credencial = credencial
        if chave:
            self.chave = chave
        if modo:
            self._url = apiurls.get(modo)
    
    def credenciar(self, dados_empresa):
        headers = self.headers_content
        response = self._post(None, headers, dados_empresa)
        if response.ok:
            info = response.json()
            self.configurar(info['credencial'], info['chave'])
        return response.text

