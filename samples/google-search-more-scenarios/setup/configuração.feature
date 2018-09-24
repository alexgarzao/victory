Funcionalidade: Configuração do teste

  @setup
  Cenário: Setup do teste
    Dado que a configuração está na tabela abaixo
      | nome                | valor |
      | HEADLESS            | false |
      | SLEEP_BETWEEN_STEPS | 100   |

    Então o teste é iniciado
