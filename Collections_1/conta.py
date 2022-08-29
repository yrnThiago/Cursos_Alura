from Alura.Collections_1.conta_corrente import Conta, ContaCorrente, ContaPoupanca, ContaInvestimento, ContaSalario
from operator import attrgetter
import array as arr
import numpy as np


conta_do_thi = ContaSalario(1700)
conta_da_ju = ContaSalario(3)
conta_do_paulo = ContaSalario(133)
conta_do_thi.deposita(500)
conta_da_ju.deposita(500)
conta_do_paulo.deposita(500)


contas = [conta_do_thi, conta_do_paulo, conta_da_ju]
print(conta_do_thi <= conta_da_ju)
