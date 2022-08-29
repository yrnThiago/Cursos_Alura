from Alura.Collections_1.conta_corrente import Conta, ContaCorrente, ContaPoupanca, ContaInvestimento, ContaSalario
from operator import attrgetter
import array as arr
import numpy as np

# TUPLAS:

# conta_do_thi_oo = ContaCorrente(10)
# print(conta_do_thi_oo)
# conta_do_thi_oo.deposita(100)
# print(conta_do_thi_oo)

# conta_do_thi = (15, 1000)
# print(conta_do_thi)


# def deposita(conta): # variação "funcional" (separando o comportamento dos dados)
#     novo_saldo = conta[1] + 100
#     codigo = conta[0]
#     return (codigo, novo_saldo)


# conta_do_thi = deposita(conta_do_thi)

# print(conta_do_thi)'''

# DUCK TYPING:

# conta16 = ContaCorrente(16)
# conta16.deposita(1000)

# conta17 = ContaPoupanca(17)
# conta17.deposita(1000)


# contas = [conta16, conta17]
# for conta in contas:
#     conta.passa_o_mes()
#     print(conta)

# array (menos usada)
# arr = arr.array('d', [1, 3.5])
# print(arr)
# numpy (geralmente usada)
# numneros = np.array([1, 3, 5])
# print(numneros - 1)

conta_do_thi = ContaSalario(1700)
conta_da_ju = ContaSalario(3)
conta_do_paulo = ContaSalario(133)
conta_do_thi.deposita(500)
conta_da_ju.deposita(500)
conta_do_paulo.deposita(500)


contas = [conta_do_thi, conta_do_paulo, conta_da_ju]
print(conta_do_thi <= conta_da_ju)
