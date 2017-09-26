#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.contadigital import ContaDigital

class Credenciamento(ContaDigital):
    """docstring for Credenciamento."""
    def __init__(self):
        super().__init__()
    
    def documentos(self, dados):
        pass
        
    def adicionar_saldo(self, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._post(None, headers, dados)
        return response.json()

    def webhook(self, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._put(None, headers, dados)
        return response.json()

    def novo_admin(self, dados):
        headers = self.headers_chave
        response = self._post(['administradores'], headers, dados)
        return response.json()

    def excluir_admin(self, email):
        headers = self.headers_chave
        response = self._delete(['administradores', email], headers)
        return response.json()