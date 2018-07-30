Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela
    Dado que quero definir os elementos da tela
    E a tela de busca é https://www.google.com/
    Então os elementos são
      | elemento          | método | identificação                                |
      | barra de busca    | xpath  | //*[@id="lst-ib"]                            |
      | botão de pesquisa | xpath  | //*[@id="tsf"]/div[2]/div[3]/center/input[1] |
