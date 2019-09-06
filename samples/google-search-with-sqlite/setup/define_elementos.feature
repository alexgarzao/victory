Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela de busca
    Dado que quero definir os elementos da tela de busca
    E a URL é https://www.google.com/
    Então os elementos são
      | elemento          | método | identificação                                        |
      | barra de busca    | xpath  | //*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input |
      | botão de pesquisa | xpath  | //*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]  |

    # Mapeamento sem parâmetros
    E a ação pesquisa é
      | evento                            |
      | Quando clico no botão de pesquisa |

    # Mapeamento com parâmetros
    E a ação pesquisa por {texto} é
      | evento                                                                                     |
      | Dado que vou para a tela de busca                                                          |
      | E preencho a barra de busca com o valor {texto}                                            |
      | Quando clico no botão de pesquisa                                                          |
      | E aguardo 1 segundo                                                                        |
      | Então sou direcionado para a url que inicia em https://www.google.com/search?source=hp&ei= |
