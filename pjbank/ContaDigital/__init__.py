#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from pjbank.ContaDigital import Administradores
from pjbank.ContaDigital import Credenciamento
from pjbank.ContaDigital import Subcontas
from pjbank.ContaDigital import Transacoes
from pjbank.ContaDigital import Recebimentos


class ContaDigital(object):
    """docstring for ContaDigital."""
    def __init__(self, arg):
        super(ContaDigital, self).__init__()
        self.arg = arg
        