Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela inicial
    Dado que quero definir os elementos da tela inicial
    E a URL é http://the-internet.herokuapp.com/nested_frames
    Então os elementos são
      | elemento         | método | identificação |
      | frame superior   | nome   | frame-top     |
      | frame inferior   | nome   | frame-bottom  |
      | frame esquerdo   | nome   | frame-left    |
      | frame do meio    | nome   | frame-middle  |
      | frame da direita | nome   | frame-right   |
