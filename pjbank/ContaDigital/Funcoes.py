#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.ContaDigital import ContaDigital


class Credenciamento(ContaDigital):
    """docstring for Credenciamento."""
    def __init__(self):
        super().__init__()
    
    def documentos(self, dados):
        pass
        
    def adicionar_saldo(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(None, headers, dados)
        return response.json

    def webhook(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._put(None, headers, dados)
        return response.json

    def novo_admin(self, dados):
        headers = self.headers_chave
        response = self._post(['administradores'], headers, dados)
        return response.json

    def excluir_admin(self, email):
        headers = self.headers_chave
        response = self._delete(['administradores', email], headers)
        return response.json


class Consultas(ContaDigital):
    """docstring for Consultas."""
    def __init__(self):
        super().__init__()
    
    def _consulta(self, endpoint=None):
        headers = self.headers_chave        
        response = self._get(endpoint, headers)
        return response.json        
        
    def dados_conta(self):
        return self._consulta()
    
    def documentos(self):
        return self._consulta(['documentos'])
    
    def status_socio(self, email):
        return self._consulta(['administradores', email])

    def administradores(self):
        return self._consulta(['administradores'])


class SubContas(ContaDigital):
    """docstring for SubContas."""
    def __init__(self):
        super().__init__()

    def novo_cartao(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['subcontas'], headers, dados)
        return response.json

    def subconta(self, subconta):
        headers = self.headers_chave.update(self.headers_content)
        response = self._get(['subcontas', subconta], headers)
        return response.json

    def adicionar_saldo(self, subconta, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['subcontas', subconta], headers, dados)
        return response.json

    def extrato(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['subcontas'], headers, dados)
        return response.json

    

    