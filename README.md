# pjbank-python-sdk
PJbank SDK para Python! :snake: :snake: :snake:

[![Build Status](https://travis-ci.org/pjbank/pjbank-python-sdk.svg?branch=master)](http://travis-ci.org/pjbank/pjbank-python-sdk)

Consulte a [documentação da API PJBank](http://docs.pjbank.com.br) para mais informações.

# Instalação

```
pip install pjbank
```

# Quickstart

```
import pjbank

conta_boleto = pjbank.Boleto()

#modo de desenvolvimento
conta_boleto.dev(True)

conta_boleto.credenciar(dados_empresa)

conta_boleto.emitir(dados_boleto)
```


![Construcao](https://openclipart.org/image/2400px/svg_to_png/231626/underconstruction.png)
