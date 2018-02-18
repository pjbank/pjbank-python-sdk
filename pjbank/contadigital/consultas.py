#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.contadigital import ContaDigital

class Consultas(ContaDigital):
    """docstring for Consultas."""
    def __init__(self):
        super().__init__()   

    @automatico    
    def dados_conta(self):
        return self._consulta()
    @automatico        
    def documentos(self):
        return self._consulta(['documentos'])
    
    @automatico    
    def status_socio(self, email):
        return self._consulta(['administradores', email])

    @automatico    
    def administradores(self):
        return self._consulta(['administradores'])