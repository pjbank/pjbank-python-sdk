# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import unittest
from datetime import datetime as datetime       
from pjbank import Boleto

class BoletoTestCase(unittest.TestCase):
    def __init__(self):
        super(BoletoTestCase, self).__init__()
        self.dados = tests.dados
        creds = dados['recebimentos']['boleto']['credenciamento']
        self.conta = pjbank.Boleto(creds['credencial'], creds['chave'])
    
    def test_dados(self):
        self.assertGreaterEqual(len(self.dados) >)
        self.assert_(self.conta.credencial)
        self.assert_(self.conta.chave)
    
    def test_dados():
        assert(len(dados) > 0)

    def test_emitir_boleto():
        dados_emis = self.dados['recebimentos']['boleto']['emitir']
        data = (datetime.date().today()+datetime.timedelta(days=1))
        dados_emis['vencimento'] = data.strftime('%m/%d/%Y')
        