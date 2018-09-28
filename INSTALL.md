# Como instalar

Existem três formas de executar as ferramentas do Victory:
- Instalando localmente
- Via Docker
- Via Vagrant

## Instalando localmente

Obs.: Este setup somente foi validado em Linux. Mas é possível instalar em Windows também.

Requisitos:
- python 3.6 ou superior
- pip
- virtualenv

Setup (Linux):

    cd <my-projects>
    git clone https://github.com/alexgarzao/victory.git
    cd victory
    virtualenv -p <python-version> <myenv>
    source <myenv>/bin/activate
    pip install -r requirements.txt
    cd victory; python setup.py install; cd ..
    victory driverupdate

Onde:

    <my-projects> deve ser trocado pelo diretório onde será baixado o projeto
    <python-version> deve ser trocado pela versão do python a ser utilizada
    <myenv> deve ser trocado com o nome da pasta que irá conter o ambiente do virtualenv

Por exemplo:

    cd projects
    git clone https://github.com/alexgarzao/victory.git
    cd victory
    virtualenv -p python3.7 .env
    source .env/bin/activate
    pip install -r requirements.txt
    cd victory; python setup.py install; cd ..
    victory driverupdate

Como executar:

Para executar o exemplo "google search", execute o seguinte comando:

    victory run web samples/google-search


Segue abaixo o passo-a-passo desta instalação:

[![asciicast](https://asciinema.org/a/cZu5s6KbYpjQYMTSUR6TnMaL1.png)](https://asciinema.org/a/cZu5s6KbYpjQYMTSUR6TnMaL1?autoplay=1)

## Via Docker

Obs.: Este setup somente foi validado em Linux. Mas é possível executar em Windows também.

Requisitos:
- docker

Como executar:

Para executar o exemplo "google search", execute o seguinte comando:

    docker run -e "MODULE=web" -e "FEATURES_PATH=samples/google-search" alexgarzao/victory

## Via Vagrant

Obs.: Este setup foi validado em Windows e Linux.

Requisitos:
- Vagrant
- VirtualBox (requisito do Vagrant)

Setup:

    cd projects
    git clone https://github.com/alexgarzao/victory.git
    cd victory/vagrant
    vagrant up

Sempre que iniciar a VM:

Neste box do vagrant existe um Ubuntu 16.04, com o XFCE. No momento, a VM inicia em modo texto (isso vai ser ajustado), requisitando user (vagrant) e password (vagrant). Após isso, inicie o X (startx). Abrindo um console no ambiente gráfico, digite os seguintes comandos:

    cd victory
    source .env/bin/activate

Para executar o exemplo "google search", execute o seguinte comando:

    victory run web samples/google-search
