#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pjbank
"""
from pjbank.api import PJBankAPI
from pjbank.contadigital import ContaDigital
from pjbank.recebimentos.boleto import Boleto
from pjbank.recebimentos.cartaocredito import CartaoCredito
from pjbank.config import __version__

conta_digital = ContaDigital()
boleto = Boleto()
cartao = CartaoCredito()