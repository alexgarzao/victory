# beeweb

Ferramenta para automação de testes. O foco inicial foi WEB, mas temos um módulo para testar API's REST.

Existem três formas de executar o beeweb:
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
    git clone https://github.com/alexgarzao/beeweb.git
    cd beeweb
    virtualenv -p <python-version> <myenv>
    source <myenv>/bin/activate
    pip install -r requirements.txt
    cd beeweb; python setup.py install; cd ..

Onde:

    <my-projects> deve ser trocado pelo diretório onde será baixado o projeto
    <python-version> deve ser trocado pela versão do python a ser utilizada
    <myenv> deve ser trocado com o nome da pasta que irá conter o ambiente do virtualenv

Por exemplo:

    cd projects
    git clone https://github.com/alexgarzao/beeweb.git
    cd beeweb
    virtualenv -p python3.7 .env
    source .env/bin/activate
    pip install -r requirements.txt
    cd beeweb; python setup.py install; cd ..

Como executar:

Para executar o exemplo "google search", execute o seguinte comando:

    beeweb run web FEATURES_PATH=samples/google-search

## Via Docker

Obs.: Este setup somente foi validado em Linux. Mas é possível executar em Windows também.

Requisitos:
- docker

Como executar:

Para executar o exemplo "google search", execute o seguinte comando:

    docker run -e "MODULE=web" -e "FEATURES_PATH=samples/google-search" alexgarzao/beeweb

## Via Vagrant

Obs.: Este setup foi validado em Windows e Linux.

Requisitos:
- Vagrant
- VirtualBox (requisito do Vagrant)

Setup:

    cd projects
    git clone https://github.com/alexgarzao/beeweb.git
    cd beeweb/vagrant
    vagrant up

Sempre que iniciar a VM:

Neste box do vagrant existe um Ubuntu 16.04, com o XFCE. No momento, a VM inicia em modo texto (isso vai ser ajustado), requisitando user (vagrant) e password (vagrant). Após isso, inicie o X (startx). Abrindo um console no ambiente gráfico, digite os seguintes comandos:

    cd beeweb
    source .env/bin/activate

Para executar o exemplo "google search", execute o seguinte comando:

    beeweb run web FEATURES_PATH=samples/google-search

Segue abaixo este exemplo sendo executado:

[![asciicast](https://asciinema.org/a/zNvoWDIJpVYxmRYdSoO9G0yRg.png)](https://asciinema.org/a/zNvoWDIJpVYxmRYdSoO9G0yRg?autoplay=1)
