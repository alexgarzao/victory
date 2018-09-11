Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela inicial
    Dado que quero definir os elementos da tela inicial
    E a URL é http://the-internet.herokuapp.com/nested_frames
    Então os elementos são
      | elemento   | método | identificação |
      | superior   | nome   | frame-top     |
      | inferior   | nome   | frame-bottom  |
      | esquerdo   | nome   | frame-left    |
      | do meio    | nome   | frame-middle  |
      | da direita | nome   | frame-right   |
