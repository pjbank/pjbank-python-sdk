#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.api import PJBankAPI
from pjbank.ContaDigital import Administradores
from pjbank.ContaDigital import Credenciamento
from pjbank.ContaDigital import Subcontas
from pjbank.ContaDigital import Transacoes
from pjbank.ContaDigital import Recebimentos


class ContaDigital(PJBankAPI):
    """docstring for ContaDigital."""
    def __init__(self, credencial=None, chave=None):
        super().__init__(credencial, chave)
        self.__endpoint_base = "contadigital"


    def credenciar(self, dados):
        if len(dados.keys) < 11:
            raise Exception("É preciso fornecer os dados de cadastro obrigatórios.")
        return super().credenciar(dados)