#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbanksdk.api import PJBankAPI

class Boleto(PJBankAPI):
    """docstring for Boleto."""
    def __init__(self):
        super(Boleto, self).__init__()
        self._endpoint = "recebimentos"
    
    def get_modelo(self, tipo):
        pass

    def credenciar(self, parametros):
        endpoint = "/".join([self._endpoint])
        response = self.request("POST", endpoint, parametros)
        if response.ok:
            info = response.json()
            self.configurar(info['credencial'], info['chave'])
        return response.text
    
    def emitir_boleto(self, parametros):
        endpoint = "/".join([self._endpoint, self._credencial, 'transacoes'])
        response = self.request("POST", endpoint, parametros)
        return response.text
    
    def imprimir_boletos_lote(self, parametros):
        header = self.post
        header["X-CHAVE"] = self._chave
        endpoint = "/".join([self._endpoint, self._credencial, 'transacoes', 'lotes'])
        response = self.request("POST", endpoint, parametros, header)
        return response.text

    def imprimir_carne(self, parametros):
        header = self.post
        header["X-CHAVE"] = self._chave
        endpoint = "/".join([self._endpoint, self._credencial, 'transacoes', 'lotes'])
        response = self.request("POST", endpoint, parametros, header)
        return response.text
        