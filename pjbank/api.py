#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pjbank.config import __apiurls__ as apiurls

class PJBankAPI(object):
    """Classe representando a API PJBank."""

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

    def dev(self, dev=True):
        if type(dev) == str and dev == 'producao':
            dev = False
        if dev == True:
            self._modo = 'sandbox'
        elif dev == False:
            self._modo = 'producao'
        self._url = apiurls.get(self._modo)
        return self.modo   
    
    @property
    def headers_chave(self):
        return {self._chave_headers: self.chave}
    
    @property
    def headers_content(self):
        return {"Content-Type": self._content_type}
    
    def _get_endpoint(self, recursos=None):
        base = [self._url, self._endpoint_base]
        if self.credencial:
            base.extend([self.credencial])
        if recursos:
            base.extend(recursos)
        url = '/'.join(base)
        return url

    def _request(self, metodo, endpoint, headers, dados=None, params=None):
        url = self._get_endpoint(endpoint)
        response = requests.request(metodo, url, json=dados, headers=headers, params=params)
        response.encoding = 'utf-8'
        return response

    def _get(self, endpoint, headers, params=None):
        return self._request("GET", endpoint, headers, params)

    def _post(self, endpoint, headers, dados, params=None):
        return self._request("POST", endpoint, headers, dados, params)

    def _put(self, endpoint, headers, dados, params=None):
        return self._request("PUT", endpoint, headers, dados, params)

    def _delete(self, endpoint, headers, dados=None, params=None):
        return self._request("DELETE", endpoint, headers, dados, params)

    def credenciar(self, dados_empresa):
        headers = self.headers_content
        response = self._post(None, headers, dados_empresa)
        info = response.json()
        if self.credencial or self.chave:
            raise Exception("Esta conta já está credenciada.".encode("utf-8")) 
        if not response.ok:
            raise Exception(response.text)
        self.credencial = info['credencial']
        self.chave = info['chave']
        self.resposta_credenciamento = info
        return info

