#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.api import PJBankAPI

class ContaDigital(PJBankAPI):
    """docstring for ContaDigital."""
    def __init__(self, credencial=None, chave=None, webhook_chave=None):
        super().__init__()
        self._endpoint_base = "contadigital"
        self._webhook_chave = webhook_chave

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

    def enviar_documento(self, dados):
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

    def novo_cartao_corporativo(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['subcontas'], headers, dados)
        return response.json

    def dados_subconta(self, subconta):
        headers = self.headers_chave.update(self.headers_content)
        response = self._get(['subcontas', subconta], headers)
        return response.json

    def adicionar_saldo_subconta(self, subconta, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['subcontas', subconta], headers, dados)
        return response.json

    def extrato_subconta(self, dados):
        headers = self.headers_chave.update(self.headers_content)
        response = self._post(['subcontas'], headers, dados)
        return response.json