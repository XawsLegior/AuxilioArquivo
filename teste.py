from Database.Database import Database

#       [!] - DESCOMENTE OS EXEMPLOS PARA TESTAR
#

""" 
-----------------------------------------------------------
    --> INSERIR APENAS 1 LINHA
    --> O VALOR Xaws/25 VAI SER INSERIDO NA PRIMEIRA LINHA
-----------------------------------------------------------
"""
#Database.insert(Database("insert into(Servidores/Config/exemplos) values(Xaws/25)"))


""" 
-----------------------------------------------------------
    --> INSERIR 2 LINHAS
    --> VAI SER INSERIDO O VALOR wk/5 NA LINHA 1
    --> E O VALOR xaws/12 NA LINHA 2
-----------------------------------------------------------
"""
#res = Database.insert(Database("insert into(Servidores/Config/exemplos) values(wk/5, xaws/12)"))
#print(res)


""" 
-----------------------------------------------------------
    --> SELECIONAR 1 DADO DE 1 LINHA
    --> VAI LER E RETORNAR O DADO INFORMADO NA LINHA INFORMADA
    --> VAMOS PEGAR O VALOR 12 DA LINHA 2
-----------------------------------------------------------
"""
#res = Database.select(Database("select 1 from Servidores/Config/exemplos where 1=xaws"))
#print(res)


""" 
-----------------------------------------------------------
    --> SELECIONAR TUDO
    --> VAMOS PEGAR TODOS OS VALORES DE UM ARQUIVO
-----------------------------------------------------------
"""
#res = Database.select(Database("select * from Servidores/Config/exemplos"))
#print(res)


""" 
-----------------------------------------------------------
    --> ATUALIZAR 1 VALOR
    --> VAMOS MUDAR O NOME DO xaws (NA LINHA2) PARA legior
-----------------------------------------------------------
"""
#res = Database.update(Database("update 1 from Servidores/Config/exemplos='legior' where 1=xaws"))
#print(res)
#res = Database.select(Database("select 1 from Servidores/Config/exemplos where 1=legior"))
#print(res)


""" 
-----------------------------------------------------------
    --> ATUALIZAR TODOS OS VALORES
    --> VAMOS MUDAR TODOS OS NOMES PARA dwk ONDE A POSIÇÃO 1 TIVER O NOME xaws
-----------------------------------------------------------
"""
#res = Database.update(Database("update * from Servidores/Config/exemplos='dwk' where 1=xaws"))
#print(res)
#res = Database.select(Database("select 1 from Servidores/Config/exemplos where 1=legior"))
#print(res)