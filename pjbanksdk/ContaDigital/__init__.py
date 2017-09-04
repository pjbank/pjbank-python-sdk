#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from pjbanksdk.ContaDigital import Administradores
from pjbanksdk.ContaDigital import Credenciamento
from pjbanksdk.ContaDigital import Subcontas
from pjbanksdk.ContaDigital import Transacoes
from pjbanksdk.ContaDigital import Recebimentos


class ContaDigital(object):
    """docstring for ContaDigital."""
    def __init__(self, arg):
        super(ContaDigital, self).__init__()
        self.arg = arg
        