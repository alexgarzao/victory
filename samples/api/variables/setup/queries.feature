Funcionalidade: Definir as queries necessárias ao teste

  Cenário: Definir a query de busca da palavra de ID 1
    Dado que quero definir a query palavra 1 para o SQLITE
    Então o arquivo de database é :memory:
    E a query é
    """
      SELECT *
          FROM dictionary
          WHERE id = 1
    """
    E obtenho o campo word

  Cenário: Definir a query de busca da palavra de ID 2
    Dado que quero definir a query palavra 2 para o SQLITE
    Então o arquivo de database é :memory:
    E a query é
    """
      SELECT *
          FROM dictionary
          WHERE id = 2
    """
    E obtenho o campo word
