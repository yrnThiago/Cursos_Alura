import re

endereco = 'Rua github, Bairro gitgit, hubhub, 12345-678'
padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
