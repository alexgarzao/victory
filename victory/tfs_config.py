import configparser


class TfsConfig():
    def __init__(self, config_filename, section):
        self.config = configparser.ConfigParser(interpolation=None)
        self.config_filename = config_filename
        self.section = section

    def read(self):
        self.config.read(self.config_filename)

    def update(self, url, area_path, user, password):
        self.config.read(self.config_filename)
        self.config[self.section] = {
            'URL': url,
            'AREA_PATH': area_path,
            'USER': user,
            'PASSWORD': password
        }

        with open(self.config_filename, 'w') as config_file:
            self.config.write(config_file)

    def url(self):
        return self.config[self.section]['URL']

    def area_path(self):
        return self.config[self.section]['AREA_PATH']

    def user(self):
        return self.config[self.section]['USER']

    def password(self):
        return self.config[self.section]['PASSWORD']
