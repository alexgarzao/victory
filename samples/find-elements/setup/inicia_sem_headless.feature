Funcionalidade: Inicia os testes sem head less

  Cenário: Setup do teste
    Dado que a configuração está na tabela abaixo
      | nome                | valor                   |
      | APP_URL             | https://www.google.com/ |
      | HEADLESS            | false                   |
      | SLEEP_BETWEEN_STEPS | 0                       |

    Então o teste é iniciado
