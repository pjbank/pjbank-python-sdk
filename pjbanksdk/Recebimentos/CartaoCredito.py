#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbanksdk.api import PJBankAPI

class CartaoCredito(PJBankAPI):
    """docstring for Boleto."""
    def __init__(self, credencial=None, chave=None):
        super(CartaoCredito, self).__init__()
        self.__endpoint_base = "recebimentos"
        self.__metodos = ["GET", "POST", "DELETE"]
        if credencial and chave:
            self.configurar(credencial, chave)

    def get_modelo(self, tipo):
        pass

    def credenciar(self, dadosEmpresa):
        response = self._post(self.get_endpoint(), self.get_headers(), dadosEmpresa)
        if not dadosEmpresa['cartao']:
            dadosEmpresa['cartao'] = True
        if response.ok:
            info = response.json()
            self.configurar(info['credencial'], info['chave'])
        return response.text

    def tokenizar(self, dadosCartao):
        response = self._post(self.get_endpoint('tokens'), self.get_headers(), dadosCartao)
        return response.text

    def imprimir(self, idsBoletos, carne=None):
        body = {"pedido_numero": idsBoletos}
        if carne:
            body.update({"formato": carne})
        response = self._post(self.get_endpoint('transacoes','lotes'), self.get_headers(), body)
        return response.text

    def extrato(self, pago=None, dataInicio=None, dataFim=None, pagina=None):
        url_params = self.get_endpoint('transacoes')
        params = {}
        if pago:
            params.update({"pago":pago})
        if dataInicio:
            params.update({"dataInicio":dataInicio})
        if dataFim:
            params.update({"dataFim":dataFim})
        if pagina:
            params.update({"pagina":pagina})

        response = self._get(url_params, self.get_headers(), params=params)
        return response.text
    