##### Esse script auxilia na manipulação de arquivos, os comandos são semelhantes ao um banco de dados relacional, e a estrutura é semelhante a um banco de dados não relacional.

### Configuração inicial
As configurações são feitas no arquivo principal (Database.py).
- extensao, formato do arquivo, por padrão é .ini
- path, caminho onde todos os arquivos/pastas serão gerados
- pastas, nesse list deve ser informado as pastas que devem ser geradas
 - deve ser informado o caminho completo, ignorando o path
 
**Exemplo:**
- pastas = ["Servidores/Config"]
 - Dentro da pasta path (Database) vai ser gerado a pasta Servidores
 - Dentro da pasta Servidores vai ser gerado a pasta Config


### Comandos
- Insert
 - insert into(**caminho**) values(l**inha1/linha1, linha2**)

- Select
 - select **posição** from **caminho**
 - select **posição** from **caminho** where **posição**=**valor**

- Update
 - update **posição** from **caminho/arquivo**='**novo valor**' where **posição**=**valor**
 - update *****  from **caminho/arquivo** where **posição**=**valor**