Funcionalidade: Realizar uma busca simples

  @smoke
  Cenário: Como usuário quero fazer uma busca simples
    Dado que quero fazer uma busca
    E estou na tela de busca
    E preencho a barra de busca com o valor XYZ
    Quando clico no botão de pesquisa
    E aguardo 1 segundo
    #TODO: Tem que implementar retentativas de validacao na URL, por isso o time de 3 segundos.
    Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei=
