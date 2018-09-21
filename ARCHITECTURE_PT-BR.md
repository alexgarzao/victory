# Arquitetura do projeto

O Victory, independente do módulo que será executado (WEB, API, ...), utiliza o Behave.
Ao iniciar sua execução, os passos executados são os seguintes:

* Carregar os steps genéricos
* Carregar o módulo e seus steps específicos
* Executar o Behave

O Behave, por sua vez, tem a seguinte linha de execução:
* Carregar config
* Carregar steps
* Carregar cenários
* Executar cenários
* Gerar saída (em ./output/)

O Victory, após a execução do Behave, pode gerar bem como enviar um report via e-mail.
