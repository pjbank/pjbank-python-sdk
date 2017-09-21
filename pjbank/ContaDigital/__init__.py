#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.api import PJBankAPI
from pjbank.ContaDigital.Funcoes import SubContas, Consultas, Credenciamento

class ContaDigital(PJBankAPI):
    """docstring for ContaDigital."""
    def __init__(self, credencial=None, chave=None, webhook_chave=None):
        super().__init__(credencial, chave)
        self._endpoint_base = "contadigital"
        self._webhook_chave = webhook_chave
        self.subcontas = SubContas()
        self.consultas = Consultas()
        self.credenciamento = Credenciamento()

    @property
    def webhook_chave(self):
        return self._webhook_chave

    @webhook_chave.setter
    def webhook_chave(self, chave):
        self._webhook_chave = chave

    def credenciar(self, dados):
        super().credenciar(dados)
        self.webhook_chave = self.resposta_credenciamento.json()['webhook_chave']
        return self
