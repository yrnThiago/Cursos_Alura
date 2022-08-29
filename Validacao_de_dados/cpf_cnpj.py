from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        quantidade_de_digitos = len(documento)
        if quantidade_de_digitos == 11:
            return DocCpf(documento)
        elif quantidade_de_digitos == 14:
            return DocCnpj(documento)

        raise ValueError("Quantidade de digitos ínválida!")


class DocCpf:
    def __init__(self, documento):
        if not self.valida(documento):
            raise ValueError("CPF inválido")

        self.cpf = documento

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        return CPF().validate(documento)

    def formata(self):
        return CPF().mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if not self.valida(documento):
            raise ValueError("CNPJ inválido")

        self.cnpj = documento

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        return CNPJ().validate(documento)

    def formata(self):
        return CNPJ().mask(self.cnpj)
