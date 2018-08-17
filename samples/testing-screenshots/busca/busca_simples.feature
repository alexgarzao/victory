Funcionalidade: Realizar uma busca simples

  Cenário: Como usuário quero fazer uma busca - screenshot de um cenário ok
    Dado que vou para a tela de busca
    E preencho a barra de busca com o valor XYZ1
    Quando clico no botão de pesquisa
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=

  @TAG1.1234 @TAG2.56789
  Cenário: Como usuário quero fazer uma busca - screenshot de um cenário com falha
    Dado que vou para a tela de busca
    E preencho a barra de busca com o valor XYZ2
    Quando executo a pesquisa
    E aguardo 1 segundo
    Então sou direcionado para a url que inicia em https://www.xxx
