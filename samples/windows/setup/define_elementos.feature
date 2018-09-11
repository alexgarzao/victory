Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela inicial
    Dado que quero definir os elementos da tela inicial
    E a URL é http://the-internet.herokuapp.com/windows
    Então os elementos são
      | elemento   | método | identificação |
      | new window | css    | .example a    |

  Cenário: Definir os elementos da nova janela
    Dado que quero definir os elementos da tela nova janela
    E a URL é http://the-internet.herokuapp.com/windows/new
