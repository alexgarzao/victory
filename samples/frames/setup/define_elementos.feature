Funcionalidade: Definir o mapeamento dos elementos da interface

  Cenário: Definir os elementos da tela inicial
    Dado que quero definir os elementos da tela inicial
    E a URL é http://the-internet.herokuapp.com/tinymce
    Então os elementos são
      | elemento | método | identificação |
      | TinyMCE  | id     | mce_0_ifr     |
      | editor   | id     | tinymce       |
