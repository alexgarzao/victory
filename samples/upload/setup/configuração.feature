Funcionalidade: Configuração do teste

  Cenário: Setup do teste
    Dado que a configuração está na tabela abaixo
      | nome                | valor |
      | HEADLESS            | false |
      | SLEEP_BETWEEN_STEPS | 100   |
      | FILES_PATH          | files |

    Então o teste é iniciado
