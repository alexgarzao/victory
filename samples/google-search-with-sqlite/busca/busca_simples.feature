Funcionalidade: Realizar uma busca simples

  Cenário: Como usuário quero fazer uma busca pela palavra de ID 1
    Dado que crio um banco para testar a execução de queries
    E que vou para a tela de busca
    E preencho a barra de busca com a consulta palavra 1
    Quando clico no botão de pesquisa
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  Cenário: Como usuário quero fazer uma busca pelapalavra de ID 2
    Dado que vou para a tela de busca
    E preencho a barra de busca com a consulta palavra 2
    Quando clico no botão de pesquisa
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=
