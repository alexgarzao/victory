Funcionalidade: Inicia os testes sem head less

  Cenário: Setup do teste
    Dado que quero realizar um teste
    E a configuração está na tabela abaixo
      | nome                | valor                   |
      | APP_URL             | https://www.google.com/ |
      | HEADLESS            | false                   |
      | SLEEP_BETWEEN_STEPS | 0                       |

    Quando tento inicializar o teste
    Então recebo um status ok
