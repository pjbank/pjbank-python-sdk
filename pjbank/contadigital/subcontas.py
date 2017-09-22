#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.contadigital import ContaDigital

class SubContas(ContaDigital):
    """docstring for SubContas."""
    def __init__(self):
        super().__init__()

    def novo_cartao(self, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._post(['subcontas'], headers, dados)
        return response.json()

    def subconta(self, subconta):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._get(['subcontas', subconta], headers)
        return response.json()

    def adicionar_saldo(self, subconta, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._post(['subcontas', subconta], headers, dados)
        return response.json()

    def extrato(self, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._post(['subcontas'], headers, dados)
        return response.json()
