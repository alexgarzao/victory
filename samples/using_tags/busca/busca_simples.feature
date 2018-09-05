Funcionalidade: Realizar uma busca simples

  @scenario1
  Cenário: Como usuário quero fazer uma busca simples - busca de elementos por xpath
    Dado que vou para a tela de busca
    E preencho a barra de busca por xpath com o valor XYZ1
    Quando clico no botão de pesquisa
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  @scenario2
  Cenário: Como usuário quero fazer uma busca simples - busca de elementos por nome
    Dado que vou para a tela de busca
    E preencho a barra de busca por nome com o valor XYZ2
    Quando clico no botão de pesquisa
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  @scenario3
  Cenário: Como usuário quero fazer uma busca simples - busca de elementos por classe
    Dado que vou para a tela de busca
    E preencho a barra de busca por classe com o valor XYZ3
    Quando clico no botão de pesquisa
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=
