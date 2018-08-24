from jinja2 import Template
import datetime
import glob

from smtp_email import SmtpEmail
from scenarios_result import ScenariosResult


TITLE = """{{project_name}}: Resultado da execução dos testes - Build {{build_id}} ({{build_status}})"""

BODY = """
<html>
  <head></head>
  <body>
O que: Resultado da execução dos testes automatizados<br>
Projeto: {{project_name}}<br>
Build: {{build_id}}<br>
Data/Hora: {{date_time}}<br>
Branch: {{branch_name}}<br>
Último commit: {{last_commit}}<br>
Total de funcionalidades: {{total_features}} ({{failed_features}} com falha)<br>
Total de cenários: {{total_scenarios}} ({{failed_scenarios}} com falha)<br>
Status: {{build_status}}<br>
Tempo de execução: {{duration}}<br>
<br>
Cenários:<br>
{{scenarios_result}}
<br>
  </body>
</html>
"""


class TfsReport:
    def __init__(self, tfs, smtp_server, email_user, email_password):
        self.tfs = tfs
        self.smtp_server = smtp_server
        self.email_user = email_user
        self.email_password = email_password

    def send_by_email(self, smtp_from, smtp_to, project_name, build_id, branch_name, last_commit):
        scenarios_result = ScenariosResult()

        context = {
            'project_name': project_name,
            'build_id': build_id,
            'branch_name': branch_name,
            'last_commit': last_commit,
            'date_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'build_status': scenarios_result.build_status,
            'total_features': scenarios_result.total_features,
            'failed_features': scenarios_result.failed_features,
            'total_scenarios': scenarios_result.total_scenarios,
            'failed_scenarios': scenarios_result.failed_scenarios,
            'duration': "{0:.2f}s".format(scenarios_result.duration),
            'scenarios_result': scenarios_result.html_table,
        }

        template = Template(TITLE)
        title = template.render(context)

        template = Template(BODY)
        body = template.render(context)

        image_list = glob.glob("./screenshots/*.png")
        email = SmtpEmail(self.smtp_server, self.email_user, self.email_password)
        return email.send(smtp_from, smtp_to, title, body, image_list)
