from pjbanksdk.api import Api
from pjbanksdk import Recebimento as RCB
from pjbanksdk import ContaDigital as CD

class PJBank(Api):
    """docstring for PJBank."""
    def __init__(self, credencial= None, chave = None, modo = "sandbox"):
        self._credencial = credencial
        self._chave = chave
        self._modo = modo
        
    def check(self, parameter_list):
        print(self._credencial)
        print(requests.__version__)
    
    def config(self):
        pass


class Recebimento(PJBank):
    """docstring for Recebimento."""
    def __init__(self, arg):
        super(Recebimento, self).__init__()
        self.arg = arg


class ContaDigital(PJBank):
    """docstring for ContaDigital."""
    def __init__(self, arg):
        super(ContaDigital, self).__init__()
        self.arg = arg
        