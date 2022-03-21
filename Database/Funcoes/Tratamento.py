class tratamento(str):
    def tratarStr(self):
        try:
            dados = self.replace("insert into", "")
            dados = dados.replace("(", "")
            dados = dados.replace(")", "")
            dados = dados.replace("select", "")
            dados = dados.replace("from", "")
            dados = dados.replace("where", "")
            dados = dados.replace("values", "")
            dados = dados.replace("  ", "\\")
            dados = dados.replace("'", "")
            dados = dados.split("\\")
            # Tratar espaço, vírgula e igual
            newDados = str()
            for index, item in enumerate(dados):
                if index <= 1:
                    dados[index] = item.replace(" ", "\\")
                    dados[index] = dados[index].replace(",", "\\")
                else:
                    dados[index] = dados[index].replace("=", "\\=\\")
                newDados += dados[index] + "\\"
            newDados = newDados.split("\\")
            # Tratar valors vazios
            for index, item in enumerate(newDados):
                if item == '':
                    newDados.pop(index)
            return newDados
        except:
            return False