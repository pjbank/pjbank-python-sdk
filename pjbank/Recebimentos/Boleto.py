#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.api import PJBankAPI

class Boleto(PJBankAPI):
    """docstring for Boleto."""
    def __init__(self, credencial=None, chave=None):
        super(Boleto, self).__init__()
        self.__endpoint_base = "recebimentos"
        self.__metodos = ["GET", "POST"]
        if credencial and chave:
            self.configurar(credencial, chave)

    def get_modelo(self, tipo):
        pass

    def credenciar(self, dados_empresa):
        response = self._post(self.get_endpoint(), self.get_headers(), dados_empresa)
        if response.ok:
            info = response.json()
            self.configurar(info['credencial'], info['chave'])
        return response.text

    def emitir(self, dados_boleto):
        response = self._post(self.get_endpoint('transacoes'), self.get_headers(), dados_boleto)
        return response.text

    def imprimir(self, ids_boletos, carne=None):
        body = {"pedido_numero": ids_boletos}
        if carne:
            body.update({"formato": carne})
        response = self._post(self.get_endpoint('transacoes', 'lotes'), self.get_headers(), body)
        return response.text

    def extrato(self, pago=None, data_inicio=None, data_fim=None, pagina=None):
        url_params = self.get_endpoint('transacoes')
        params = {}
        if pago:
            params.update({"pago":pago})
        if data_inicio:
            params.update({"data_inicio":data_inicio})
        if data_fim:
            params.update({"data_fim":data_fim})
        if pagina:
            params.update({"pagina":pagina})

        response = self._get(url_params, self.get_headers(), params=params)
        return response.text
    