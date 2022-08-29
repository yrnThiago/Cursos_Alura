from typing import Union

from Alura.PEP8.fila_normal import FilaNormal
from Alura.PEP8.fila_prioritaria import FilaPrioritaria
from Alura.PEP8.constante import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:

    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError("Tipo de fila não existe!")
