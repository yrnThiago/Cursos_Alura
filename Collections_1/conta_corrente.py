from abc import ABCMeta, abstractmethod
from functools import total_ordering


class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"

    @abstractmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.5
        self._saldo -= 3.5


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'>>Código {self._codigo} Saldo {self._saldo}<<'

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo


class ContaMultiploSalarios(ContaSalario):
    pass
