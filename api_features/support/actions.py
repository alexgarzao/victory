from .fields import Fields
from .http_status_codes import HttpStatusCodeAliasList
from .api import Api


class Action(object):
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

    def get_field_by_name(self, name):
        return self.field_list.get_by_name(name)

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
        elif self.method == 'PUT':
            self.api.put(self.__get_url(), self.parameters)
        else:
            assert False

    def check_result(self, status_code):
        self.api.validar_retorno(status_code)

    def __get_url(self):
        path = self.__replace_parameters(self.path, self.parameters)
        return self.base_url + '/' + path

    def __replace_parameters(self, text, parameters):
        for parameter, value in parameters.items():
            if type(value) is not str and type(value) is not int:
                continue
            field = self.get_field_by_name(parameter)
            token_to_find = "{" + field.alias + "}"
            text = text.replace(token_to_find, str(value))

        return text


class ActionList(object):
    def __init__(self):
        self.__action_list = {}

    def add(self, base_url, alias):
        action = Action(base_url, alias)
        self.__action_list[alias] = action
        return action

    def get(self, alias):
        return self.__action_list[alias]
