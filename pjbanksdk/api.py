import requests
from pjbanksdk.config import __endpoint_map__

class Api(object):
    """docstring for PJBank."""
    def __init__(self, credencial = None, chave = None, modo = None):
        super(PJBank, self).__init__()
        if credencial:
            self._credencial = credencial
        if chave:             
            self._chave = chave
        if modo:
            self._endpoint = self.__endpoint_map__.get(modo)
        if not self._endpoint:
            self._endpoint = self.__endpoint_map__.get("sandbox")
    
    def request(self, parametros):
        # self.header = self.getHeader()
        # self.body
        # return requests.request()
        pass


    def getHeader(self, metodo, padrao = "padrao"):
        permitidos = ["GET", "POST", "DELETE"]
        if metodo not in permitidos:
            raise ValueError("Método {} não é permitido. Utilize {}".format(metodo, ",".join(permitidos)))
        get = {"X-CHAVE": self._chave}
        post = {"Content-Type": "application/x-www-form-urlencoded"}
        delete = {"X-CHAVE": self._chave}
        headers = {"GET": get, "POST": post, "DELETE": delete}
        return headers[metodo][padrao]

    def body(self, parameter_list):
        pass
    
    def data(self, parameter_list):
        pass
