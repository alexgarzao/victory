Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela
    Dado que quero definir os elementos da tela
    Então o elemento barra de busca tem o xpath //*[@id="lst-ib"]
    E o elemento botão de pesquisa tem o xpath //*[@id="tsf"]/div[2]/div[3]/center/input[1]
    E a tela de busca é https://www.google.com/

    # Mapeamento sem parâmetros
    E o evento tento pesquisar é
      | evento                            |
      | Quando clico no botão de pesquisa |

    # Mapeamento com parâmetros
    E o evento faço a pesquisa por {texto} é
      | evento                                                                               |
      | Dado que vou para a tela de busca                                                         |
      | E preencho a barra de busca com o valor {texto}                                        |
      | Quando clico no botão de pesquisa                                                           |
      | E aguardo 1 segundo                                                                    |
      | Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei= |

    # # Abordagem mais complexa
    # E o evento tento me logar com o usuário {user} e senha {password} é
    #   | evento                                    |
    #   | o elemento {user} tem o id user           |
    #   | o elemento {password} tem o id j_password |
    #   | clico no botão login                      |
