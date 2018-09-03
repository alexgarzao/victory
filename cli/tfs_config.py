import configparser


class TfsConfig():
    CONFIG_FILE = "./config.ini"

    def update(self, url, area_path, user, password):
        config = configparser.ConfigParser(interpolation=None)
        config.read(TfsConfig.CONFIG_FILE)
        config['TFS'] = {
            'URL': url,
            'AREA_PATH': area_path,
            'USER': user,
            'PASSWORD': password
        }

        with open(TfsConfig.CONFIG_FILE, 'w') as config_file:
            config.write(config_file)
