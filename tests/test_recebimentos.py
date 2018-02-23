# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import unittest
import pickle
import datetime
import random    
from pjbank import Boleto
from dados import dados

class DadosTeste(object):
    def __init__(self):
        super(DadosTeste, self).__init__()
        self._dados = dados
    
    @property
    def dados(self):
        return self._dados
        
        
class BoletoTestCase(unittest.TestCase):
    def setUp(self):
        self.dados = DadosTeste().dados
        creds = self.dados['recebimentos']['boleto']['credenciamento']
        self.boleto = Boleto(creds['credencial'], creds['chave'])
    
    def test_dados(self):
        self.assertGreaterEqual(len(self.dados), 0)
        self.assert_(self.boleto.credencial)
        self.assert_(self.boleto.chave)
    
    
    def emitir_boleto(self, dados, random_pedido=False):
        if random_pedido:
            dados['pedido_numero'] = random.randint(1000,99999)
        return self.boleto.emitir(dados)
        

    def test_emitir_boleto(self):
        dados_emis = self.dados['recebimentos']['boleto']['emitir']
        data = (datetime.date.today()+datetime.timedelta(days=1))
        dados_emis['vencimento'] = data.strftime('%m/%d/%Y')
        res = self.emitir_boleto(dados_emis, True)
        response = res.json()
        self.assertIn("id_unico", response)
        self.assertIn("nossonumero", response)
        self.assertIn("banco_numero", response)
        self.assertIn("linkBoleto", response)
        self.assertIn("linkGrupo", response)
        self.assertIn("linhaDigitavel", response)
    
    def test_editar_boleto(self):
        dados_emis = self.dados['recebimentos']['boleto']['emitir']
        bol = self.emitir_boleto(dados_emis, True)
        bol.r = bol.json()
        self.assertEqual(bol.r['status'], '201')
        dados_emis['valor'] = 50.50
        dados_emis['pedido_numero'] = bol.r['pedido_numero']
        bol2 = self.emitir_boleto(dados_emis, False)
        bol.r = bol.json()
        self.assertEqual(bol.r["linkBoleto"], bol2.r["linkBoleto"])
        self.assertEqual(bol.r["linkGrupo"], bol2.r["linkGrupo"])
        self.assertEqual(bol.r["linhaDigitavel"], bol2.r["linhaDigitavel"])
    
        
        
        