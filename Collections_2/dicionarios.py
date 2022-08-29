from collections import defaultdict, Counter

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# | & - ^ -> operadores para conjuntos

fez_ds_mas_nao_fez_ml = usuarios_machine_learning ^ usuarios_data_science
print(fez_ds_mas_nao_fez_ml)

# frozenset -> conjunto imutavel

fez_ds_mas_nao_fez_ml = frozenset(fez_ds_mas_nao_fez_ml)

aparicoes = {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}
for i, x in aparicoes.items():
    print(i, x)


# defaultdict -> Chave ter um valor padrão

dicionario = defaultdict(int)
print(dicionario['Teste'])

# Counter(i) -> Contador

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
aparicoes = Counter(meu_texto.split())
print(aparicoes)

# Testando o uso de diversas coleções

texto_1 = '''
Por fim, vamos colocar tudo isso em prática para vermos algum exemplo diferente? Então o que eu queria fazer agora não é um contador de palavras, eu fazer um contador de letras para vermos uma coisa interessante que acontece na língua portuguesa e em outras línguas, para ser sincero, também. Então eu vou criar aqui uma nova sessão que é "#Testando o uso de diversas coleções".
'''

texto_2 = '''
Então eu quero copiar o texto em português sobre programação e mais um pouco aqui, copiar tudo isso. Então eu tenho um texto, que é um texto razoável, posso rodar, é um texto sobre programação e vou colocar um texto2 também, três aspas, Enter. E agora um texto sobre B2C, B2B, e por aí vai. Então vou pegar esse texto aqui, e olha, tem bastante texto, tem bastante texto mesmo. Não é programação, então vou copiar todo esse texto, porque não falou de programação. Copiei.
'''


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    for caractere, proporcao in proporcoes.most_common(10):
        print(f'{caractere} => {proporcao * 100:.2f}%')


analisa_frequencia_de_letras(texto_1)
analisa_frequencia_de_letras(texto_2)

