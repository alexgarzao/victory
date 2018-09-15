Funcionalidade: Cadastro de imóveis

# TODO: Setup do teste sempre que troca de feature.

  Cenário: Como usuário quero confirmar que não tenho imóveis no momento
    Dado que quero listar imóveis
    Quando tento executar
    Então recebo o status OK
    E obtenho uma lista vazia

  Esquema do Cenário: Como usuário quero cadastrar imóveis com dados válidos
    Dado que quero cadastrar um imóvel
    E o campo nome do proprietário é <nome do proprietário>
    E o campo características do imóvel é <características>
    E o campo endereço do imóvel é <endereço>
    E o campo valor do imóvel é <valor>
    E o campo está ocupado é <está ocupado>
    Quando tento executar
    Então recebo o status imóvel criado com sucesso
    E salvo o resultado em <variável>

    Exemplos: Dados válidos para imóveis
      | nome do proprietário | está ocupado | características | endereço                             | valor  | variável |
      | Proprietário 01      | sim          | A,B,C,D         | Rua A Porto Alegre Rio Grande do Sul | 1000.0 | imóvel1  |
      | Proprietário 02      | não          | <nulo>          | Rua B Porto Alegre Rio Grande do Sul | 2000.0 | imóvel2  |
      | Proprietário 03      | não          | <nulo>          | Rua C Porto Alegre Rio Grande do Sul | 3000.0 | imóvel3  |

  Cenário: Como usuário quero confirmar que agora tenho 3 imóveis cadastrados
    Dado que quero listar imóveis
    Quando tento executar
    Então recebo o status OK
    E obtenho a lista de dados abaixo
    | nome do proprietário | está ocupado | características do imóvel | endereço do imóvel                   | valor do imóvel |
    | Proprietário 01      | sim          | A,B,C,D                   | Rua A Porto Alegre Rio Grande do Sul | 1000.0          |
    | Proprietário 02      | não          | <nulo>                    | Rua B Porto Alegre Rio Grande do Sul | 2000.0          |
    | Proprietário 03      | não          | <nulo>                    | Rua C Porto Alegre Rio Grande do Sul | 3000.0          |

  Cenário: Como usuário quero alterar o imóvel do proprietario 2
    Dado que quero alterar um imóvel
    E o campo id do imóvel é $imóvel2.id_imovel
    E o campo nome do proprietário é Novo Proprietário
    Quando tento executar
    Então recebo o status imóvel alterado com sucesso

  Cenário: Como usuário quero confirmar que o imóvel foi alterado
    Dado que quero listar imóveis
    Quando tento executar
    Então recebo o status OK
    E obtenho a lista de dados abaixo
    | nome do proprietário | está ocupado | características do imóvel | endereço do imóvel                   | valor do imóvel |
    | Proprietário 01      | sim          | A,B,C,D                   | Rua A Porto Alegre Rio Grande do Sul | 1000.0          |
    | Novo Proprietário    | não          | <nulo>                    | Rua B Porto Alegre Rio Grande do Sul | 2000.0          |
    | Proprietário 03      | não          | <nulo>                    | Rua C Porto Alegre Rio Grande do Sul | 3000.0          |





  # Cenário: Como usuário quero listar meus imóveis cadastrados (dados errados).
  #   Dado que eu quero listar os meus imóveis
  #   Quando eu busco a lista de imóveis
  #   Então eu recebo o status que indica requisição válida
  #   E obtenho a lista de dados abaixo
  #   | nome do proprietário | está ocupado | características do imóvel | endereço do imóvel                   | valor do imóvel |
  #   | Proprietário 08      | sim          | A,B,C,D                   | Rua A Porto Alegre Rio Grande do Sul | 1000.0          |
  #   | Proprietário 02      | não          | <nulo>                    | Rua C Porto Alegre Rio Grande do Sul | 2000.0          |


    # | nome do proprietário | data de cadastro | está ocupado | características | endereço                             | valor   |
    # | Proprietário 01      | <nao nulo>       | sim          | 1,2,3,4         | Rua A Porto Alegre Rio Grande do Sul | 1000.00 |
    # | Proprietário 02      | <nao nulo>       | nao          | <nulo>          | Rua B Porto Alegre Rio Grande do Sul | 2000.00 |
