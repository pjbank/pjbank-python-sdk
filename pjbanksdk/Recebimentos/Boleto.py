#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbanksdk.api import PJBankAPI

class Boleto(PJBankAPI):
    """docstring for Boleto."""
    def __init__(self):
        super(Boleto, self).__init__()
        self.__endpointBase = "recebimentos"
        self.__metodos = ["GET", "POST"]
    
    def get_modelo(self, tipo):
        pass
    
    def get_headers(self, chave=None):
        headers = {"Content-Type":"application/json"}
        if chave:
            headers.update({"X-CHAVE": self.get_chave})
        return headers
            
    def get_endpoint(self, *args):
        if self._credencial:
            args = [self._credencial]+args
        return "/".join([self.__endpointBase]+args)

    def credenciar(self, dadosEmpresa):
        response = self._post(self.get_endpoint(), self.get_headers(), dadosEmpresa)
        if response.ok:
            info = response.json()
            self.configurar(info['credencial'], info['chave'])
        return response.text
    
    def emitir(self, dadosBoleto):
        response = self._post(self.get_endpoint('transacoes'), self.get_headers(), dadosBoleto)
        return response.text
    
    def imprimir(self, idsBoletos, carne=None):
        body = {"pedido_numero": idsBoletos}
        if carne:
            body.update({"formato": carne})
        response = self._post(self.get_endpoint('transacoes','lotes'), self.get_headers(), body)
        return response.text
    
    def extrato(self, pago=None, dataInicio=None, dataFim=None, pagina=None):
        url_params = self.get_endpoint('transacoes')
        params = {"pago":pago, "dataInicio": dataInicio, "dataFim": dataFim, "pagina": pagina}
        response = self._get(url_params, self.get_headers(), params=params)
        return response.text