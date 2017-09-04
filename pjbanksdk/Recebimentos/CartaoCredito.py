#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbanksdk.api import PJBankAPI

class CartaoCredito(PJBankAPI):
    """docstring for Boleto."""
    def __init__(self):
        super(CartaoCredito, self).__init__()
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
    
    def tokenizar(self, parametros):
        header = self.post
        header["X-CHAVE"] = self._chave
        endpoint = "/".join([self._endpoint, self._credencial, 'tokens'])
        response = self.request("POST", endpoint, parametros, header)
        return response.text
    
    def transacao(self, parametros):
        header = self.post
        header["X-CHAVE"] = self._chave
        endpoint = "/".join([self._endpoint, self._credencial, 'transacoes'])
        response = self.request("POST", endpoint, parametros, header)
        return response.text
        
    def cancelar_transacao(self, id_operacao):
        endpoint = "/".join([self._endpoint, self._credencial, 'transacoes', id_operacao])
        response = self.request("DELETE", endpoint, None)
        return response.text