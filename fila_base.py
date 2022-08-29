import abc
from Alura.PEP8.constante import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO
from typing import List


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ''

    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1
