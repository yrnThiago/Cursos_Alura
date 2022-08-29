from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        dia_nascimento, mes_nascimento, ano_nascimento = self._data_nascimento.split('/')
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split()
        return nome_quebrado[-1]

    def _eh_socio(self):
        return self.sobrenome() in ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu'] and self._salario >= 100000

    def decrescimo_salario(self):
        if self. _eh_socio():
            return self._salario - self._salario * 0.1

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito para receber um bônus!')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
