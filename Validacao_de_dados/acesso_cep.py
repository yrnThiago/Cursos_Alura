import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP é inválido!")

    def __str__(self):
        return self.formata_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self):
        dados = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/').json()
        return dados['bairro'], dados['localidade'], dados['uf']

