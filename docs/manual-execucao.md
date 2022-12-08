# Manual de execução

Neste manual você encontra o passo a passo de como colocar o projeto para rodar
localmente em sua máquina.

Caso esteja usando windows, substitua `python3` por `py` nos comandos em que
essa palavra aparece.

## Requisitos

Você precisa ter o [python](https://www.python.org/) instalado em sua máquina.

## Executando o projeto

### Download do código fonte

Faça o download do código fonte na [página inicial do repositório](https://github.com/labens-ufrn/academic-devflow),
caso escolha baixar em formato .zip, lembre-se de descompactar o arquivo após o
download.

Em seguida abra a pasta com o código em uma interface de linha de comando, de
acordo com as instruções abaixo.

No windows:

1. Abra a pasta do projeto no explorador de arquivos
2. Selecione o caminho da pasta na parte superior da janela
3. Digite `cmd` e aperte `enter`

No linux:

1. Abra a pasta do projeto no seu explorador de arquivos
2. Clique com o botão direito do mouse e selecione a opção `Abrir no terminal`

### Criando o ambiente virtual

Na linha de comando, execute o comando `python3 -m venv .venv`.

Aguarde o ambiente ser criado e em seguida o ative.

No linux: `source .venv/bin/activate`

No windows: `.venv\Scripts\activate`

Você sabe que o ambiente está ativado quando o texto `(.venv)` aparece no início
do caminho mostrado pela linha de comando.

### Instalando as dependências

Com o ambiente virtual ativado, execute `pip install -r requirements.txt`.

Depois aplique as migrações executando `python3 manage.py makemigrations` e
`python3 manage.py migrate`.

### Iniciando o servidor local

Execute o comando `python3 manage.py runserver`.

O servidor será iniciado no endereço `localhost:8000`, para pará-lo basta ir na
linha de comando e apertar `Ctrl C`.
