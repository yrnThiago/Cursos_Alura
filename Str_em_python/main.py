from Alura.Str_em_python.extracao import URL

url = URL('bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real')
moeda_origem = url.get_valor_params('moedaOrigem')
moeda_destino = url.get_valor_params('moedaDestino')
quantidade = url.get_valor_params('quantidade')
print(url.converter_dolar_real(moeda_origem, moeda_destino, quantidade))
