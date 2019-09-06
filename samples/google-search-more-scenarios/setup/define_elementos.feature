Funcionalidade: Definir o mapeamento dos elementos da interface

  @setup
  Cenário: Definir os elementos da tela de busca
    Dado que quero definir os elementos da tela de busca
    E a URL é https://www.google.com/
    Então os elementos são
      | elemento          | método | identificação                                        |
      | barra de busca    | xpath  | //*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input |
      | botão de pesquisa | xpath  | //*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]  |
