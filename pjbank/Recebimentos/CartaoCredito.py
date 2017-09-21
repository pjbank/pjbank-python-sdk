#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.Recebimentos import Recebimentos

class CartaoCredito(Recebimentos):
    """docstring for CartaoCredito."""
    def __init__(self, credencial=None, chave=None):
        super().__init__(credencial, chave)

    def credenciar(self, dados):
        dados.update({'cartao': True})
        return super().credenciar(dados)
    
    def tokenizar(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['tokens'], headers, dados)
        return response.text

    def transacao(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['transacoes'], headers, dados)
        return response.text

    def cancelar(self, id_operacao):
        headers = self.headers_chave
        response = self._delete(['transacoes', id_operacao], headers)
        return response.text
