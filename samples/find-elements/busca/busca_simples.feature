Funcionalidade: Realizar uma busca simples

  @smoke
  Cenário: Como usuário quero fazer uma busca simples - busca de elementos por xpath
    Dado que estou na tela de busca
    E preencho a barra de busca por xpath com o valor XYZ1
    Quando clico no botão de pesquisa por xpath
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  @smoke
  Cenário: Como usuário quero fazer uma busca simples - busca de elementos por nome
    Dado que vou para a tela de busca
    E preencho a barra de busca por nome com o valor XYZ2
    Quando clico no botão de pesquisa por xpath
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  @smoke
  Cenário: Como usuário quero fazer uma busca simples - busca de elementos por classe
    Dado que vou para a tela de busca
    E preencho a barra de busca por classe com o valor XYZ3
    Quando clico no botão de pesquisa por xpath
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  # @smoke
  # Cenário: Como usuário quero fazer uma busca simples - busca de elementos por ID
  #   Dado que vou para a tela de busca
  #   E preencho a barra de busca por id com o valor XYZ4
  #   Quando clico no botão de pesquisa por xpath
  #   E aguardo 1 segundo
  #   Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=
