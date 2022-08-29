from typing import Union

from Alura.PEP8.fila_base import FilaBase
from Alura.PEP8.constante import CODIGO_PRIORITARIO
from Alura.PEP8.estatistica_detalhada import EstatisticaDetalhada
from Alura.PEP8.estatistica_resumida import EstatisticaResumida

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)

        return f'Cliente atual: {cliente_atual} - Caixa {caixa}'

    def estatistica(self, retorna_estatistica: Classes) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)

