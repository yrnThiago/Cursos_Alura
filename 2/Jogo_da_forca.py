from random import randint


def mensagem_inicio():
    print('********************')
    print('***Jogo da Forca!***')
    print('********************')


def define_palavra_secreta():
    with open('palavras_secretas.txt') as arq:
        arq = arq.readlines()
    palavras = [palavra.strip() for palavra in arq]
    return palavras[randint(0, len(palavras)-1)].upper()


def mostra_letras_certas(x):
    return ["_" for _ in x]


def jogador_chute():
    return input('Digite uma letra: ').strip().upper()


def verifica_letra_jogador(letra_jogador, letras_acertadas, palavra_secreta):
    index = 0
    for letra_palavra in palavra_secreta:
        if letra_jogador == letra_palavra:
            letras_acertadas[index] = letra_jogador
            print(f'Encontrei a letra {letra_jogador} na posição {index}.')
        index += 1


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    mensagem_inicio()

    palavra_secreta = define_palavra_secreta()

    letras_acertadas = mostra_letras_certas(palavra_secreta)

    enforcou, acertou = False, False
    erros = 0

    while not enforcou and not acertou:
        if letras_acertadas.count('_') > 0:
            letra_jogador = jogador_chute()
            print('Jogando...')

            if letra_jogador in palavra_secreta:
                verifica_letra_jogador(letra_jogador, letras_acertadas, palavra_secreta)
            else:
                erros += 1
                desenha_forca(erros)
            print(' '.join(letras_acertadas))

        else:
            acertou = True

        if erros == 7:
            enforcou = True

    if acertou:
        mensagem_vencedor()
    elif enforcou:
        mensagem_perdedor(palavra_secreta)


if __name__ == "__main__":
    jogar()

