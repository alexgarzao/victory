Funcionalidade: Queries
  Contexto:
    Dado que crio um banco para testar a execução de queries

  Cenário: Obter dados de queries e guardar em variáveis
    E que $var1 = $query:palavra 1
    E que $var2 = $query:palavra 2
    Quando consulto o valor de $var1
    Então obtenho o valor XXX10
    Quando consulto o valor de $var2
    Então obtenho o valor XXX20

  Cenário: Consultar pelo nome do campo no hora de executar a query
    Dado que $var11 = $query:registro 2.word
    E que $var12 = $query:registro 2.number
    Quando consulto o valor de $var11
    Então obtenho o valor XXX20
    Quando consulto o valor de $var12
    Então obtenho o valor 2000

  Cenário: Consultar pelo nome do campo na hora de obter o resultado
    Dado que $var21 = $query:registro 2
    Quando consulto o valor de $var21.word
    Então obtenho o valor XXX20
    Quando consulto o valor de $var21.number
    Então obtenho o valor 2000
