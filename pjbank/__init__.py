#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pjbank
"""
from pjbank.api import PJBankAPI
from pjbank.ContaDigital import ContaDigital as ContaDigital
from pjbank.Recebimentos.Boleto import Boleto as Boleto
from pjbank.Recebimentos.CartaoCredito import CartaoCredito as Cartao
from pjbank.config import __version__


class PJBank(PJBankAPI):
    """docstring for PJBank."""
    def __init__(self):
        self._contadigital = ContaDigital
        self._boleto = Boleto
        self._cartao = Cartao
    
    @property
    def contadigital(self):
        return self._contadigital

    @contadigital.setter
    def contadigital(self, credencial, chave):
        self._contadigital = self._contadigital(credencial, chave)

    @property
    def boleto(self):
        return self._boleto

    @boleto.setter
    def boleto(self, credencial, chave):
        self._boleto = self._boleto(credencial, chave)

    @property
    def cartao(self):
        return self._cartao

    @cartao.setter
    def cartao(self, credencial, chave):
        self._cartao = self._cartao(credencial, chave)

    @classmethod
    def credenciar(cls, produto, dados):
        produtos = {"conta digital": cls.contadigital, "boleto": cls.boleto, "cartao": cls.cartao}
        produtoPJ = produtos.get(produto)
        response = produtoPJ.credenciar(dados)
        return response
    