import re
from Database.Funcoes.Tratamento import tratamento

class comandos:
    #+++++++++++++++++++++++++++++++++ INSERT +++++++++++++++++++++++++++++++++#
    def inserir(self, dados):
        path = dados[1][0]
        extensao = dados[0][0]
        try:
            strTratada = tratamento.tratarStr(tratamento(self))
            if strTratada is False : return False
            arquivo = path + "/" + strTratada[0] + extensao
            strTratada.pop(0)
            f = open(arquivo, "a")
            for item in strTratada:
                f.write(item)
                f.write("\n")
            f.close()
            return True
        except:
            return False

    # +++++++++++++++++++++++++++++++++ SELECT +++++++++++++++++++++++++++++++++#
    def selecionar(self, config):
        path = config[1][0]
        extensao = config[0][0]
        dados = tratamento.tratarStr(tratamento(self))
        ler = dados[0]
        arquivo = f"{path}/{dados[1]}{extensao}"
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

    # +++++++++++++++++++++++++++++++++ UPDATE +++++++++++++++++++++++++++++++++#
    def atualizar(self, config):
        path = config[1][0]
        extensao = config[0][0]
        dados = tratamento.tratarStr(tratamento(self))
        if dados[1] == "*":
            dados[2] = dados[2].split("=")
            caminho = dados[2][0]
            atualizar = dados[2][1]
            index_where = int(dados[3]) - 1
            f = open(f"{path}/{caminho}{extensao}", "r")
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

                novaLista += "\n"
            novaLista = novaLista.replace("\n\n", "\n")
            f = open(f"{path}/{caminho}{extensao}", "w")
            f.write(novaLista)
            f.close()
            return True
        else:  # UPDATE DADO ESPECIFICO
            dados[2] = dados[2].split("=")
            index = int(dados[1]) - 1
            index_where = int(dados[3]) - 1
            f = open(f"{path}/{dados[2][0]}{extensao}", "r+")
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

                    newLista += item_f_update + "/"
                newLista = newLista[0:-1]
                newLista += "\n"
            newLista = newLista[0:len(newLista) - 1]  # Remover barra do final
            newLista = newLista.replace("\\n", "\n")

            f.truncate(0)
            f.seek(0)
            f.write(newLista)
            f.close()
            return True