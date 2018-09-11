Funcionalidade: Fazer o upload de um arquivo

  # Based on this: http://elementalselenium.com/tips/1-upload-a-file
  Cenário: Como usuário quero fazer o upload de um arquivo
    Dado que vou para a tela inicial
    E faço o upload do arquivo dogs no file upload
    E clico no file submit
    Então verifico que a página tem o conteúdo File Uploaded!
    E aguardo 1 segundo
