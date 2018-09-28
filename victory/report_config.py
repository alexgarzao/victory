import configparser


class ReportConfig():
    def __init__(self, config_filename, section):
        self.config = configparser.ConfigParser(interpolation=None)
        self.config_filename = config_filename
        self.section = section

    def read(self):
        self.config.read(self.config_filename)

    def update(self, project_name, smtp_server, smtp_from, smtp_to, username, password):
        self.config.read(self.config_filename)
        self.config[self.section] = {
            'PROJECT_NAME': project_name,
            'SMTP_SERVER': smtp_server,
            'SMTP_FROM': smtp_from,
            'SMTP_TO': smtp_to,
            'USERNAME': username,
            'PASSWORD': password
        }

        with open(self.config_filename, 'w') as config_file:
            self.config.write(config_file)

    def project_name(self):
        return self.config[self.section]['project_name']

    def smtp_server(self):
        return self.config[self.section]['smtp_server']

    def smtp_from(self):
        return self.config[self.section]['from']

    def smtp_to(self):
        return self.config[self.section]['to']

    def username(self):
        return self.config[self.section]['username']

    def password(self):
        return self.config[self.section]['password']

    def replace_if_necessary(self, project_name, smtp_server, smtp_from, smtp_to, username, password):
        if project_name:
            self.config[self.section]['project_name'] = project_name

        if smtp_server:
            self.config[self.section]['smtp_server'] = smtp_server

        if smtp_from:
            self.config[self.section]['smtp_from'] = smtp_from

        if smtp_to:
            self.config[self.section]['smtp_to'] = smtp_to

        if username:
            self.config[self.section]['username'] = username

        if password:
            self.config[self.section]['password'] = password
