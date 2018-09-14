Funcionalidade: Login

# TODO: Setup do teste sempre que troca de feature.

  Cenário: Como usuário tento me logar com a senha correta
    Dado que quero logar
    E o campo usuário é usuario@usuario.com
    E o campo senha é 'senha usuario@usuario.com'
    Quando tento executar
    Então recebo o status login válido
