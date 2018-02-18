#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.api import PJBankAPI

class Recebimentos(PJBankAPI):
    """docstring for Recebimentos."""
    def __init__(self, credencial=None, chave=None):
        super().__init__(credencial, chave)
        self._endpoint_base = "recebimentos"
        self._chave_headers = "X-CHAVE"
        
    def extrato(self, pago=None, data_inicio=None, data_fim=None, pagina=None):
        params = {}
        if pago:
            params.update({"pago":pago})
        if data_inicio:
            params.update({"data_inicio":data_inicio})
        if data_fim:
            params.update({"data_fim":data_fim})
        if pagina:
            params.update({"pagina":pagina})

        headers = self.headers_chave.update(self.headers_content)
        response = self._get(['transacoes'], headers, params=params)
        return response.text