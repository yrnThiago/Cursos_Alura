import re


class TelefoneBr:

    def __init__(self, telefone):
        if not self.valida_telefone(telefone):
            raise ValueError('Número incorreto!')

        self.numero = telefone

    def __str__(self):
        return self.formata_numero()

    def valida_telefone(self, telefone):
        padrao = '(\d{2,3})?([(]?\d{2}[)]?)(\d{4,5})[-]?(\d{4})'
        resposta = re.search(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def formata_numero(self):
        padrao = '([0-9]{2})?([(]?[0-9]{2}[)]?)([0-9]{4,5})[-]?([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        numero_formatado = f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'

        return numero_formatado
