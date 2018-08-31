class TestConfig(object):
    def __init__(self):
        self.configs = {}
        self.__set_defaults()

    def set(self, name, value):
        assert name in ('HEADLESS', 'SLEEP_BETWEEN_STEPS', 'FILES_PATH')
        self.configs[name] = value

    def get_string(self, name, default=""):
        return self.configs.get(name, default)

    def get_bool(self, name, default="False"):
        return self.configs.get(name, default).upper() == "TRUE"

    def get_number(self, name, default="0"):
        return int(self.configs.get(name, default))

    def __set_defaults(self):
        self.set('HEADLESS', 'False')
        self.set('SLEEP_BETWEEN_STEPS', '0')
