Funcionalidade: Configuração do teste

  Cenário: Setup do teste
    Dado que a configuração está na tabela abaixo
      | nome                | valor                           |
      | BINARY              | C:/windows/system32/notepad.exe |
      | SERVER              | http://192.168.56.101:9999      |
      | SLEEP_BETWEEN_STEPS | 100                             |

    Então o teste é iniciado
