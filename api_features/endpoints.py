from api_features.fields import Fields
from api_features.http_status_codes import HttpStatusCodeAliasList
from api_features.api import Api


class Endpoint(object):
    def __init__(self, base_url, alias):
        self.base_url = base_url
        self.alias = alias
        self.field_list = Fields()
        self.http_status_code_alias_list = HttpStatusCodeAliasList()
        self.path = None
        self.method = None
        self.parameters = {}
        self.api = Api()

    def set_path(self, value):
        self.path = value

    def set_method(self, value):
        self.method = value

    def add_field(self, name, type, field):
        self.field_list.add(name, type, field)

    def get_field(self, name):
        return self.field_list.get(name)

    def add_status_code_alias(self, http_status_code, alias):
        self.http_status_code_alias_list.add(http_status_code, alias)

    def get_status_code(self, alias):
        return self.http_status_code_alias_list.get(alias)

    def send(self):
        # print("Method: {}\nURL: {}\nParameters: {}\n".format(self.method, self.__get_url(), self.parameters))
        if self.method == 'POST':
            self.api.post(self.__get_url(), self.parameters)
        elif self.method == 'GET':
            self.api.get(self.__get_url())
        else:
            assert False

    def check_result(self, status_code):
        self.api.validar_retorno(status_code)

    def __get_url(self):
        return self.base_url + '/' + self.path


class EndpointList(object):
    def __init__(self):
        self.__endpoint_list = {}

    def add(self, base_url, alias):
        endpoint = Endpoint(base_url, alias)
        self.__endpoint_list[alias] = endpoint
        return endpoint

    def get(self, alias):
        return self.__endpoint_list[alias]
