#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pjbank
"""
from pjbank import ContaDigital, Recebimentos
from pjbank.config import __version__


class PJBank(object):
    """docstring for PJBank."""
    def __init__(self):
        self._boleto = Recebimentos.Boleto
        self._cartao = Recebimentos.CartaoCredito

    @classmethod
    def boleto(self, credencial, chave):
        return  self._boleto(credencial, chave)
    
    @classmethod
    def cartao(self, credencial, chave):
        return  self._cartao(credencial, chave)
