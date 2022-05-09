### Ambientes virtuais com venv

#### [Home](../../../index.md) | [Python](../index.md)

Para gerenciar bibliotecas com o utilitário _*venv*_, os princiais passos são os seguintes:

1. Escolher um diretório, dentro do qual será criado o seu ambiente virtual.

1. No terminal do Linux, ou no prompt de comando do Windows, navegar até o diretório escolhido e criar o ambiente, com o comando:

```bash
$python -m venv <nome_escolhido_para_o_ambiente>
```

3. Após este comando, será criado um diretório, dentro da pasta, com o nome escolhido.

1. A próxima etapa é ativar o ambiente virtual, o que pode ser feito com os comandos a seguir:

- No Linux

```bash
$source <nome_escolhido_para_o_ambiente>/bin/activate
```

- No Windows

```powershell
><nome_escolhido_para_o_ambiente>\Scripts\activate.bat
```
5. Em seguida, devem ser instalados os pacotes necessários para o projeto. Para tanto, salve no mesmo diretório do projeto um arquivo, com o nome requirements.txt, dentro do qual deverão ser relacionados os pacotes. Após, use o comando:

```
$pip install -r requirements.txt

# Se o comando pip não funcionar, pode ser que ele precise ser executado de outra forma:
$python -m pip install -r requirements.txt
```

Com a execução bem sucedida da instalação, o ambiente estará em condições para uso. Toda vez que precisar instalar novas bibliotecas, é necessário atualizar o arquivo requirements.txt, para que possa ser usado em outros projetos semelhantes. Ou para que possa descrever as dependências do projeto no github, sem precisar que as bibliotecas sejam enviadas para o repositório remote.

Para atualizar o conteúdo do requirements.txt, basta executar:

```
$pip freeze > requirements.txt

# ou então
$python -m pip freeze > requirements.txt
```