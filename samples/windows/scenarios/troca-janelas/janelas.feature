Funcionalidade: Múltiplas janelas (windows)

  # Based on this: http://elementalselenium.com/tips/4-work-with-multiple-windows
  Cenário: Como usuário quero lidar com várias janelas
    Dado que vou para a tela inicial
    E verifico que a página tem o conteúdo Opening a new window
    Quando clico em new window
    Então sou direcionado para uma nova janela com a tela nova janela
    E verifico que a página tem o conteúdo New Window
    E volto para a janela anterior com a tela inicial
    E verifico que a página tem o conteúdo Opening a new window
    E aguardo 1 segundo
