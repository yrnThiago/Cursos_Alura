import re

endereco = 'Rua José Eduardo Ferreira dos Santos, Jd. Cruzeiro do Sul, São Paulo, 12234-814'
padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
