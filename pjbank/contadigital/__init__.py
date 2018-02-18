#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.api import PJBankAPI
import credenciamento
import consultas
import transacoes
import subcontas
from pjbank.recebimentos import Recebimentos

class ContaDigital(PJBankAPI):
    """docstring for ContaDigital."""
    def __init__(self, credencial=None, chave=None, webhook_chave=None):
        super().__init__(credencial, chave)
        self._endpoint_base = "contadigital"
        self._webhook_chave = webhook_chave
        self._recebimentos()

    def _recebimentos(self):
        self.recebimentos.boleto = Boleto(self.credencial, self.chave)
        self.recebimentos.boleto._endpoint_base = "contadigital/recebimentos"
        self.recebimentos.boleto._chave_headers = "X-CHAVE-CONTA"
        
        self.recebimentos.cartao = CartaoCredito(self.credencial, self.chave)
        self.recebimentos.cartao._endpoint_base = "contadigital/recebimentos"
        self.recebimentos.cartao._chave_headers = "X-CHAVE-CONTA"

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
        super().credenciar(dados)
        self.webhook_chave = self.resposta_credenciamento['webhook_chave']
        return self