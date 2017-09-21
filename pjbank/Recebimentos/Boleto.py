#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.Recebimentos import Recebimentos

class Boleto(Recebimentos):
    """docstring for Boleto."""
    def __init__(self, credencial=None, chave=None):
        super().__init__(credencial, chave)
    
    def credenciar(self, dados):
        dados.pop('cartao', None)
        return super().credenciar(dados)

    def emitir(self, dados):
        headers = self.headers_content
        response = self._post(['transacoes'], headers, dados)
        return response.text

    def imprimir(self, ids_boletos, carne=None):
        headers = self.headers_chave.update(self.headers_content)
        dados = {"pedido_numero": ids_boletos}
        if carne:
            dados.update({"formato": carne})
        response = self._post(['transacoes', 'lotes'], headers, dados)
        return response.text