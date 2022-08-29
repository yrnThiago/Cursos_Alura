from Alura.Validacao_de_dados.cpf_cnpj import Documento
from Alura.Validacao_de_dados.telefone_celular import TelefoneBr
from Alura.Validacao_de_dados.datas import DatasBr
from Alura.Validacao_de_dados.acesso_cep import BuscaEndereco

cep = 12234814
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)
