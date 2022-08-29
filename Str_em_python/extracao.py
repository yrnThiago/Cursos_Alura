import re


class URL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        if not re.match('(http(s)?://)?(www.)?bytebank.com?(.br)?/cambio', self.url):
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_params(self):
        indice_interrogacao = self.url.find("?")
        url_params = self.url[indice_interrogacao + 1:]
        return url_params

    def get_valor_params(self, parametro_busca):
        indice_param = self.get_url_params().find(parametro_busca)
        indice_valor = indice_param + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_params().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_params()[indice_valor:]
        else:
            valor = self.get_url_params()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'{self.url}\nParâmetros: {self.get_url_params()}\nURL Base: {self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url

    VALOR_DOLAR = 5.10

    def converter_dolar_real(self, moeda_origem, moeda_destino, quantidade):
        quantidade = float(quantidade)
        sigla_moeda_origem = 'R$'
        sigla_moeda_destino = 'US$'
        if moeda_origem == 'dolar' and moeda_destino == 'real':
            sigla_moeda_origem = 'US$'
            sigla_moeda_destino = 'R$'

        return f'{sigla_moeda_origem}{quantidade:.2f} equivale a {sigla_moeda_destino}{float(quantidade) * self.VALOR_DOLAR:.2f}\n(Conversão atual: $1.00 = R${self.VALOR_DOLAR:.2f})'
