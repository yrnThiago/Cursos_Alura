class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Contruindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo R${self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor
        print(f'Depositando R${valor} na conta do titular {self.__titular}')

    def __pode_sacar(self, valor_para_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_para_sacar <= valor_disponivel_para_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f'Sacando R${valor} da conta do titular {self.__titular}')
        else:
            print(f'O valor R${valor} passou o limite!')

    def transfere(self, valor, destino):
        print(f'Transferindo R${valor} de {self.__titular} para {destino}')
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        print('Chamando @property limite()')
        return self.__limite

    @limite.setter
    def limite(self, limite):
        print('Chamando @setter limite()')
        self.__limite = limite

    CODIGO = '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print('Chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando setter nome()')
        self.__nome = nome
