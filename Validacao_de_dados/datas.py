from datetime import datetime, timedelta


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses_do_ano = ["janeiro", "fevereiro", "março",
                        "abril", "maio", "junho",
                        "julho", "agosto", "setembro",
                        "outubro", "novembro", "dezembro"]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = ["segunda", "terça", "quarta",
                            "quinta", "sexta", "sabado",
                            "domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada

    def tempo_de_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
