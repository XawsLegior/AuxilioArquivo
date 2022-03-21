import os.path, re
from Database.Funcoes.Comandos import comandos

#########################################################
#   SCRIPT PARA AUXILIAR NA MANIPULAÇÃO DE ARQUIVOS
#   ACESSE A DOCUMENTAÇÃO AQUI -> https://github.com/XawsLegior/AuxilioArquivo/wiki/Auxilio-a-Manipulação-de-Arquivos
#
#   https://github.com/XawsLegior/AuxilioArquivo
#########################################################

class Database(str):

    def insert(self):
        res = comandos.inserir(self, dados)
        return res

    def select(self):
        res = comandos.selecionar(self, dados)
        return res

    def update(self):
        res = comandos.atualizar(self, dados)
        return res


if __name__ == 'Database.Database':
    # CARREGAR CONFIGURAÇÕES #
    config = open("Database/Config.ini", "r")
    configs = config.readlines()
    config.close()
    dados = []
    for dado in configs:
        config = re.search('=[ "\w.\[\]\/,]+', dado).group()
        config = config.replace("\"", "")
        config = config.replace("=", "")
        config = config.replace(" ", "")
        config = config.replace("[", "")
        config = config.replace("]", "")
        try:
            config = config.split(",")
        except:
            pass
        dados.append(config)
    path = dados[1][0]
    # CHECAR E GERAR PASTAS #
    # DEFINA AQUI AS PASTAS QUE DEVEM SER GERADAS #
    for pasta in dados[2]:
        if not os.path.isdir(f"{path}/{pasta}"):
            os.makedirs(f"{path}/{pasta}")