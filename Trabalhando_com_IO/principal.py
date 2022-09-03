try:
    with open('dados/contatos-n.csv', encoding='utf-8') as arquivo_contatos:
        for linha in arquivo_contatos:
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado!')
except PermissionError:
    print('Sem permissão de escrita!')
finally:
    arquivo_contatos.close()
