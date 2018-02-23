#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.api import PJBankAPI
from pjbank.recebimentos.boleto import Boleto
from pjbank.recebimentos.cartaocredito import CartaoCredito

class ContaDigital(PJBankAPI):
    """docstring for ContaDigital."""
    def __init__(self, credencial=None, chave=None, webhook_chave=None):
        super(ContaDigital, self).__init__(credencial, chave)
        self._endpoint_base = "contadigital"
        self._webhook_chave = webhook_chave
        self._recebimentos()

    def _recebimentos(self):
        self.boleto = Boleto(self.credencial, self.chave)
        self.boleto._endpoint_base = "contadigital/recebimentos"
        self.boleto._chave_headers = "X-CHAVE-CONTA"
        
        self.cartao = CartaoCredito(self.credencial, self.chave)
        self.cartao._endpoint_base = "contadigital/recebimentos"
        self.cartao._chave_headers = "X-CHAVE-CONTA"

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

    @property
    def webhook_chave(self):
        return self._webhook_chave

    @webhook_chave.setter
    def webhook_chave(self, chave):
        self._webhook_chave = chave

    def credenciar(self, dados):
        super(ContaDigital, self).credenciar(dados)
        self.webhook_chave = self.resposta_credenciamento['webhook_chave']
        return self