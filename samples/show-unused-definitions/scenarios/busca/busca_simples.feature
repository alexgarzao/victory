Funcionalidade: Realizar uma busca simples

  Cenário: Como usuário quero fazer uma busca - sem mapeamento de eventos
    Dado que vou para a tela de busca
    E preencho a barra de busca com o valor XYZ1
    Quando clico no botão de pesquisa
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  Cenário: Como usuário quero fazer uma busca - com mapeamento sem parâmetros
    Dado que vou para a tela de busca
    E preencho a barra de busca com o valor XYZ2
    Quando executo a pesquisa
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  Cenário: Como usuário quero fazer uma busca - com mapeamento com parâmetros
    Então executo a pesquisa por XYZ3
