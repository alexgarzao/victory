# Como executar

Ao executar o victory, com o comando "--help", ele lista os possíveis comandos:

    victory --help

    Usage: victory [OPTIONS] COMMAND [ARGS]...

    Options:
      --debug / --no-debug
      --stop-on-error / --dont-stop-on-error
      --help                          Show this message and exit.

    Commands:
      drivertest
      driverupdate
      run
      sendreport
      stepscatalog


* Comando drivertest e driverupdate: servem para verificar se existe uma atualização do webdriver bem como baixá-la;
* Comando run: serve para executar os cenários de teste. Neste comando deve ser informado qual o módulo que deve ser carregado (WEB ou API). Mais informações sobre este comando logo abaixo;
* Comando sendreport: serve para coletar os dados da última execução e enviar um report por e-mail. A configuração do servidor de smtp bem como para quem deve ser enviado o report é lido do arquivo config.ini. Mas estes parâmetros também podem ser passados para sendreport;
* Comando stepscatalog: serve para listar os steps disponíveis de um módulo específico.


## Comando run

Para exemplificar, vamos usar a estrutura de diretórios do exemplo google-search-more-scenarios:

    samples/google-search-more-scenarios
    ├── scenarios
    │   ├── busca1
    │   │   └── busca_simples.feature
    │   └── busca2
    │       └── busca_simples.feature
    └── setup
        ├── configuração.feature
        └── define_elementos.feature

Para executar todos os cenários:

    victory run web samples/google-search-more-scenarios

Para executar os cenários de um diretório:

    victory run web samples/google-search-more-scenarios busca2

Para executar os cenários de vários diretórios:

    victory run web samples/google-search-more-scenarios busca2 busca1

Para executar os cenários conforme uma ou mais tags:

    victory run web samples/google-search-more-scenarios --tags=cenario1,cenario2

Para executar um cenário específico:

    victory run web samples/google-search-more-scenarios busca1/busca_simples.feature

Para executar mais de um cenário:

    victory run web samples/google-search-more-scenarios busca2/busca_simples.feature busca1/busca_simples.feature
