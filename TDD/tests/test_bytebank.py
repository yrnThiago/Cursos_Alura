from Alura.TDD.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        assert Funcionario('Teste', '13/03/2000', 1111).idade()

    def test_quando_sobrenome_recebe_Thiago_Ribeiro_deve_retornar_Ribeiro(self):
        assert Funcionario('Thiago Ribeiro', '27/05/2002', 1500).sobrenome() == 'Ribeiro'

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        assert Funcionario('Paulo Bragança', '14/02/1986', 100000).decrescimo_salario() == 90000

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_10(self):
        assert Funcionario('Thiago Ribeiro', '27/05/2002', 1000).calcular_bonus() == 100

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            assert Funcionario('Thiago Ribeiro', '27/05/2002', 1000000).calcular_bonus()
