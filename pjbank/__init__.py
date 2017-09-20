#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pjbank
"""
from pjbank.api import PJBankAPI
from pjbank.ContaDigital import ContaDigital as conta_digital
from pjbank.Recebimentos.Boleto import Boleto as boleto
from pjbank.Recebimentos.CartaoCredito import CartaoCredito as cartao
from pjbank.config import __version__


class PJBank(object):
    """docstring for PJBank."""
    def __init__(self):
        self._conta_digital = conta_digital()
        self._boleto = boleto()
        self._cartao = cartao()

    @property
    def conta_digital(self):
        return self._conta_digital

    @property
    def boleto(self):
        return self._boleto

    @property
    def cartao(self):
        return self._cartao
