Funcionalidade: Login

# TODO: Setup do teste sempre que troca de feature.

  Cenário: Como usuário tento me logar com uma senha inválida
    Dado que quero executar o login
    E o campo usuário é usuario@usuario.com
    E o campo senha é 'senha invalida'
    Quando tento executar
    Então recebo o status login inválido
