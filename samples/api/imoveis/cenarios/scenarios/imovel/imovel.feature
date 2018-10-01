Funcionalidade: Cadastro de imóveis

# TODO: Setup do teste sempre que troca de feature.

  Cenário: Como usuário quero inicializar os dados do banco
    Dado que quero inicializar o banco
    Quando tento executar
    Então recebo o status banco inicializado

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
    E o campo id do imóvel é $var:imóvel2.id do imóvel
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

  Cenário: Como usuário quero consultar os dados do terceiro imóvel
    Dado que quero consultar um imóvel
    E o campo id do imóvel é $var:imóvel3.id do imóvel
    Quando tento executar
    Então recebo o status imóvel obtido com sucesso
    E o campo nome do proprietário tem o valor Proprietário 03
    E o campo características do imóvel tem o valor <nulo>
    E o campo endereço do imóvel tem o valor Rua C Porto Alegre Rio Grande do Sul
    E o campo valor do imóvel tem o valor 3000.0
    E o campo está ocupado tem o valor não

  Cenário: Como usuário quero remover o segundo imóvel
    Dado que quero remover um imóvel
    E o campo id do imóvel é $var:imóvel2.id do imóvel
    Quando tento executar
    Então recebo o status imóvel removido com sucesso

  Cenário: Como usuário quero confirmar que tenho somente dois imóveis agora
    Dado que quero listar imóveis
    Quando tento executar
    Então recebo o status OK
    E obtenho a lista de dados abaixo
    | nome do proprietário | está ocupado | características do imóvel | endereço do imóvel                   | valor do imóvel |
    | Proprietário 01      | sim          | A,B,C,D                   | Rua A Porto Alegre Rio Grande do Sul | 1000.0          |
    | Proprietário 03      | não          | <nulo>                    | Rua C Porto Alegre Rio Grande do Sul | 3000.0          |
