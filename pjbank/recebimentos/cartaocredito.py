#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.recebimentos import Recebimentos

class CartaoCredito(Recebimentos):
    """docstring for CartaoCredito."""
    def __init__(self, credencial=None, chave=None):
        super(CartaoCredito, self).__init__(credencial, chave)

    def automatico(f):
        def wrapper(self, *args, **kwargs):
            if 'c' in kwargs.keys():
                self.credencial = kwargs['c']
                kwargs.pop('c')
            if 'ch' in kwargs.keys():
                self.chave = kwargs['ch']
                kwargs.pop('ch')
            return f(self, *args, **kwargs)
        return wrapper

    def credenciar(self, dados):
        dados.update({'cartao': True})
        return super(CartaoCredito, self).credenciar(dados)

    @automatico
    def tokenizar(self, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._post(['tokens'], headers, dados)
        return response.json()

    @automatico
    def nova_transacao(self, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._post(['transacoes'], headers, dados)
        return response.json()

    @automatico
    def cancelar(self, id_operacao):
        headers = self.headers_chave
        response = self._delete(['transacoes', id_operacao], headers)
        return response.json()
