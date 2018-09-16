# Para cada recurso (endpoint)
    # eu tenho um conjunto de campos
    # tenho os possiveis status_code
    # Para cada método, tenho um path

Funcionalidade: Definir os recursos da API

  Cenário: Definindo o recurso login
    Dado que quero definir o recurso login
    # TODO: se necessario separar em campos da requisicao e reposta
    E os campos são
      | nome          | tipo    | campo no json |
      | id do usuário | integer | id_usuario    |
      | usuário       | string  | usuario       |
      | email         | string  | email         |
      | senha         | string  | senha         |
    E os códigos de retorno são
      | código | status         |
      | 204    | login válido   |
      | 404    | login inválido |
    Quando o evento é logar
    Então o método é POST
    E o path é /login

  Cenário: Definindo o recurso imóvel
    Dado que quero definir o recurso imóvel
    E os campos são
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
      | código | status                      |
      | 200    | imóvel alterado com sucesso |
      | 201    | imóvel criado com sucesso   |
      | 200    | OK                          |
      | 200    | imóvel obtido com sucesso   |
      | 204    | imóvel removido com sucesso |
    Quando o evento é cadastrar um imóvel
    Então o método é POST
    E o path é /imoveis
    Quando o evento é alterar um imóvel
    Então o método é PUT
    E o path é /imoveis/{id do imóvel}
    Quando o evento é listar imóveis
    Então o método é GET
    E o path é /imoveis
    Quando o evento é consultar um imóvel
    Então o método é GET
    E o path é /imoveis/{id do imóvel}
    Quando o evento é remover um imóvel
    Então o método é DELETE
    E o path é /imoveis/{id do imóvel}
