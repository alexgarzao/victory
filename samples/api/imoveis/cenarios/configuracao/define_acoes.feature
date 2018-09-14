Funcionalidade: Definir as ações

  Cenário: Definindo logar
    Dado que quero definir o logar
    E o path é /login
    E o método é POST

    Então os campos são
      | nome          | tipo    | campo no json |
      | id do usuário | integer | id_usuario    |
      | usuário       | string  | usuario       |
      | email         | string  | email         |
      | senha         | string  | senha         |

    E os códigos de retorno são
      | código | status         |
      | 204    | login válido   |
      | 404    | login inválido |

  Cenário: Definindo cadastrar um imóvel
    Dado que quero definir o cadastrar um imóvel
    E o path é /imoveis
    E o método é POST

    Então os campos são
      | nome                      | tipo        | campo no json   |
      | id do imóvel              | integer     | id_imovel       |
      | id do usuário             | integer     | id_usuario      |
      | endereço do imóvel        | string      | endereco        |
      | características do imóvel | string_list | caracteristicas |
      | nome do proprietário      | string      | proprietario    |
      | valor do imóvel           | number      | valor           |
      | está ocupado              | bool        | esta_ocupado    |
      | data de cadastro          | date        | data_cadastro   |

    E os códigos de retorno são
      | código | status                    |
      | 201    | imóvel criado com sucesso |
      # | 201    | elemento criado           |
      # | 204    | elemento excluído         |
      # | 200    | elemento atualizado       |
      # | 200    | elemento obtido           |
      # | 404    | elemento não encontrado   |
      # | 400    | requisição inválida       | #TODO: onde ficam os status code genéricos?
      # | 200    | requisição ok             |

  Cenário: Definindo listar imóveis
    Dado que quero definir o listar imóveis
    E o path é /imoveis
    E o método é GET

    Então os campos são
      | nome                      | tipo        | campo no json   |
      | id do imóvel              | integer     | id_imovel       |
      | id do usuário             | integer     | id_usuario      |
      | endereço do imóvel        | string      | endereco        |
      | características do imóvel | string_list | caracteristicas |
      | nome do proprietário      | string      | proprietario    |
      | valor do imóvel           | number      | valor           |
      | está ocupado              | bool        | esta_ocupado    |
      | data de cadastro          | date        | data_cadastro   |

    E os códigos de retorno são
      | código | status |
      | 200    | OK     |
