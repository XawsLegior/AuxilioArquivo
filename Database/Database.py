import os.path, re
from Database.Funcoes.Tratamento import tratamento
#########################################################
#       SEMELHANÇA AO PADRÃO DO BANCO DE DADOS RELACIONAL
#
# =====> INSERT
# => insert into(caminho) values(linha1/linha1, linha2)
#
# =====> SELECT
# => select posição from caminho
# Se no arquivo idioma.ini houver o seguinte valor english/12345
# => select 1 from caminho/idioma
# retorna english
# posição 2 retorna 12345
# posição 3 retorna false
# => select * from caminho
# retorna english/12345
#
# Arquivo reino.ini tem valor em mais de 1 linha
# XawsLegior/100/599/199000
# SwaxLegior/100/599/199000
# => select posição from caminho/reino where 1='XawsLegior'
# retorna XawsLegior
# posição 2 retorna 100
# posição 3 retorna 599
# posição 4 retorna 199000
# posição 5 retorna false
#
# =====> UPDATE
# update posição from caminho/arquivo='valor'
# pra dar update em tudo use * em posição
# pra dar update na linha de baixo apenas coloque a posição, exemplo:
# no arquivo teste.ini tem os valores:
# aaa/bbb
# bbb/ddd
# update 3 from caminho/arquivo='ccc'
# resultado
# aaa/bbb
# ccc/ddd
#########################################################

class Database(str):

    extensao = ".ini" # Extensão dos arquivos
    path = "Database" # Pasta onde tudo vai ser gerado

    def Existe(self):
        return os.path.exists(self)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def insert(self):
        try:
            dados = tratamento.tratarStr(tratamento(self))
            if dados is False : return False
            arquivo = Database.path + "/" + Database(dados[0]) + Database.extensao
            dados.pop(0)
            f = open(arquivo, "a")
            for item in dados:
                f.write(item)
                f.write("\n")
            f.close()
            return True
        except:
            return False

    def select(self):
        dados = tratamento.tratarStr(tratamento(self))
        ler = dados[0]
        arquivo = f"{Database.path}/{dados[1]}{Database.extensao}"
        tamanho = len(dados)
        try:
            f = open(arquivo, "r")
        except:
            return False

        if tamanho == 2: ### SELECT SEM WHERE
            try:  # select item
                if ler == '*':  # Select *
                    dados = f.read()
                    dados = dados.split("\n")
                    if dados[-1] == "":
                        dados.pop(-1)
                    return dados
                else:  # Select item
                    dados = f.readlines()
                    dados = dados[0].split("/")
                    return dados[int(ler) - 1].replace("\n", "")
            except:
                return False
        else:  # SELECT COM WHERE
            try:
                dadosArquivo = f.readlines()
                acao = dados[3]
                indexBuscado = -1
                for index, item in enumerate(dadosArquivo):
                    item = item.split("/")
                    for checar in item:
                        checar = checar.replace("\n", "")
                        # Checar se igual
                        if acao == "=":
                            if checar == dados[4]:
                                indexBuscado = index
                                break

                if indexBuscado == -1:
                    return False

                ### Checar se o index achado está na posição do where
                ### Exemplo, 1 = valor
                ### checar se indexBuscado é = 1
                if re.search(dados[4], dadosArquivo[indexBuscado]):
                    dadosArquivo = dadosArquivo[indexBuscado].split("/")
                    index = int(dados[0])-1
                    return dadosArquivo[index]
                return False
            except:
                return False

    def update(self):
        dados = tratamento.tratarStr(tratamento(self))
        if dados[1] == "*":
            dados[2] = dados[2].split("=")
            caminho = dados[2][0]
            atualizar = dados[2][1]
            index_where = int(dados[3]) - 1
            f = open(f"{path}/{caminho}{Database.extensao}", "r")
            novaLista = str()
            for index, item in enumerate(f):
                itemSplited = item.split("/")
                try:
                    if itemSplited[index_where] == dados[5] or itemSplited[index_where] == dados[5] + "\n":
                        for item_a in itemSplited:
                            item_a = atualizar
                            novaLista += item_a + "/"
                    else:
                        novaLista += item + "/"
                except:
                    novaLista += item + "/"
                    pass
                if novaLista[-1] == "/":
                    novaLista = novaLista[0:-1]

                novaLista+="\n"
            novaLista = novaLista.replace("\n\n", "\n")
            f = open(f"{path}/{caminho}{Database.extensao}", "w")
            f.write(novaLista)
            f.close()
            return True
        else: # UPDATE DADO ESPECIFICO
            dados[2] = dados[2].split("=")
            index = int(dados[1]) - 1
            index_where = int(dados[3]) - 1
            f = open(f"{path}/{dados[2][0]}{Database.extensao}", "r+")
            dadosArquivo = f.read().split("\n")

            atualizar = dados[2][1]
            newLista = str()
            item_sub = int(dados[1]) - 1
            for index, item in enumerate(dadosArquivo):
                item = item.split("/")
                for index_i, item_f_update in enumerate(item):
                    if int(index_where) == index_i:
                        if item[index_where] == dados[5] and item_sub == index_i:
                            item_f_update = atualizar
                    elif int(item_sub) == index_i and item[index_where] == dados[5]:
                        item_f_update = atualizar

                    newLista+= item_f_update + "/"
                newLista = newLista[0:-1]
                newLista+="\n"
            newLista = newLista[0:len(newLista)-1] # Remover barra do final
            newLista = newLista.replace("\\n", "\n")

            f.truncate(0)
            f.seek(0)
            f.write(newLista)
            f.close()
            return True


if __name__ == 'Database.Database':
    # CHECAR E GERAR PASTAS #
    # DEFINA AQUI AS PASTAS QUE DEVEM SER GERADAS #
    path = Database.path
    pastas = ["Servidores/Config"]

    for caminho in pastas:
        if not os.path.isdir(f"{path}/{caminho}"):
            os.makedirs(f"{path}/{caminho}")