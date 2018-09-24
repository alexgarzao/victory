Funcionalidade: Digitar um texto no frame

  # Based on this: http://elementalselenium.com/tips/3-work-with-frames
  Cenário: Como usuário quero digitar o texto AAA123 no frame
    Dado que vou para a tela inicial
    Então sou direcionado para o frame TinyMCE
    E preencho o editor com o valor AAA123
    E sou direcionado para o frame anterior
    E aguardo 1 segundo
