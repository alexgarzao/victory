Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela inicial
    Dado que quero definir os elementos da tela inicial
    E a URL é http://the-internet.herokuapp.com/download
    Então os elementos são
      | elemento | método | identificação |
      | arquivo  | css    | .example a    |
