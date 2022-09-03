arquivo_contatos = open('dados/contatos.csv', encoding='utf-8')

conteudo = arquivo_contatos.readlines()

for linha in conteudo:
    print(linha, end='')
