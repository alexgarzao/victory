Funcionalidade: Variáveis

  Cenário: Armazenar o resultado de uma variável
    Dado que quero definir variáveis
    Então defino que var1 igual a valorvar1

  Cenário: Obter o resultado de uma variável
    Dado que quero consultar o valor de var1
    Então obtenho o valor valorvar1

  Cenário: Definir e consultar variáveis
    Dado que var2 = valorvar2
    E que $var3 = valorvar3
    E que $var4 = $var:var3
    Quando consulto o valor de $var2
    Então obtenho o valor valorvar2
    Quando consulto o valor de var3
    Então obtenho o valor valorvar3
    Quando consulto o valor de var4
    Então obtenho o valor valorvar3

  Cenário: Obter dados de queries e guardar em variáveis
    Dado que crio um banco para testar a execução de queries
    E que $var11 = $query:palavra 1
    E que $var12 = $query:palavra 2
    Quando consulto o valor de $var11
    Então obtenho o valor XXX10
    Quando consulto o valor de $var12
    Então obtenho o valor XXX20


  # TODO: exemplos com json, pegando subcampos, ...


  #
  #   Quando eu obtenho o resultado da variável ESTADO_RESULTADO_2.nome
  #   Então eu obtenho o valor estado 2
  #   Quando eu obtenho o resultado da variável ESTADO_RESULTADO_2.sigla
  #   Então eu obtenho o valor s2
  #
  # Esquema do Cenário: Armazenar o resultado de várias requisições
  #   Dado que eu quero consultar um estado
  #   Quando eu tento consultar o estado <id>
  #   Então eu recebo o código <codigo>
  #   E o resultado deve ser salvo em <variavel>
  #
  #   Exemplos: Dados dos estados.
  #     | id | codigo | variavel    |
  #     | 1  | 200    | RESULTADO_1 |
  #     | 2  | 200    | RESULTADO_2 |
  #     | 3  | 200    | RESULTADO_3 |
  #
  # Esquema do Cenário: Obter o resultado das variáveis
  #   Dado que eu quero obter o resultado de uma variável
  #   Quando eu obtenho o resultado da variável <variavel>
  #   Então eu obtenho o valor <valor>
  #
  #   Exemplos: Dados esperados das variáveis.
  #     | variavel          | valor    |
  #     | RESULTADO_1.nome  | estado 1 |
  #     | RESULTADO_2.nome  | estado 2 |
  #     | RESULTADO_3.nome  | estado 3 |
  #     | RESULTADO_1.sigla | s1       |
  #     | RESULTADO_2.sigla | s2       |
  #     | RESULTADO_3.sigla | s3       |
