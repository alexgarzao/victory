Funcionalidade: Cadastro dos tipos de imóveis

  Cenário: Como usuário quero cadastrar os tipos de imóveis
    Dado que quero cadastrar os tipos de imóveis
    E a lista de dados do campo tiposImoveis está na tabela abaixo
    | id do tipo | descrição do tipo |
    | 1          | residencial       |
    | 2          | comercial         |
    Quando tento executar
    Então recebo o status tipos criados com sucesso
