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
        self.get = {"X-CHAVE": self._chave}
        self.post = {"Content-Type": "application/x-www-form-urlencoded"}
        self.delete = {"X-CHAVE": self._chave}
        self.metodos = ["GET", "POST", "DELETE"]
    
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

    def request(self, metodo, endpoint, parametros, header=None):
        if not header:
            header = self.get_header(metodo)
        url = "/".join([self._url, endpoint])
        return requests.request(metodo,
                                url,
                                data=parametros,
                                headers=header)

    def get_header(self, metodo):
        if metodo not in self.metodos:
            raise ValueError("Método {} não é permitido. Utilize {}".format(metodo, ",".join(self.metodos)))
        headers = {"GET": self.get, "POST": self.post, "DELETE": self.delete}
        return headers[metodo]

    def set_header(self, metodo):
        pass
