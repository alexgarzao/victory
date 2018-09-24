Funcionalidade: Buscar elementos nos frames

  # Based on this: http://elementalselenium.com/tips/3-work-with-frames
  Cenário: Como usuário quero buscar elementos nos frames
    Dado que vou para a tela inicial

    Então sou direcionado para o frame superior
    Então sou direcionado para o frame esquerdo
    E verifico que a página tem o conteúdo LEFT
    E sou direcionado para o frame anterior

    Então sou direcionado para o frame superior
    Então sou direcionado para o frame do meio
    E verifico que a página tem o conteúdo MIDDLE
    E sou direcionado para o frame anterior

    Então sou direcionado para o frame superior
    Então sou direcionado para o frame da direita
    E verifico que a página tem o conteúdo RIGHT
    E sou direcionado para o frame anterior

    Então sou direcionado para o frame inferior
    E verifico que a página tem o conteúdo BOTTOM
    E sou direcionado para o frame anterior

    E aguardo 1 segundo
