from .api import Api


class Event(object):
    def __init__(self, resource):
        self.resource = resource
        self.path = None
        self.method = None
        self.parameters = {}
        self.result = {}
        self.api = Api()

    def set_path(self, value):
        self.path = value

    def set_method(self, value):
        self.method = value

    def send(self):
        # print("Method: {}\nURL: {}\nParameters: {}\n".format(self.method, self.__get_url(), self.parameters))
        if self.method == 'POST':
            self.api.post(self.__get_url(), self.parameters)
        elif self.method == 'GET':
            self.api.get(self.__get_url())
        elif self.method == 'PUT':
            self.api.put(self.__get_url(), self.parameters)
        elif self.method == 'DELETE':
            self.api.delete(self.__get_url(), self.parameters)
        else:
            assert False

        if self.api.retorno.status_code >= 200 and self.api.retorno.status_code <= 201 and self.api.retorno.text:
            self.result = self.api.retorno.json()
        else:
            self.result = {}

    def check_result(self, status_code):
        self.api.validar_retorno(status_code)

    def __get_url(self):
        path = self.__replace_parameters(self.path, self.parameters)
        return self.resource.base_url + '/' + path

    def __replace_parameters(self, text, parameters):
        for parameter, value in parameters.items():
            if type(value) is not str and type(value) is not int:
                continue
            field = self.resource.get_field_by_name(parameter)
            token_to_find = "{" + field.alias + "}"
            text = text.replace(token_to_find, str(value))

        return text


class EventList(object):
    def __init__(self):
        self.__event_list = {}

    def add(self, alias, resource):
        event = Event(resource)
        self.__event_list[alias] = event
        return event

    def get(self, alias):
        return self.__event_list[alias]

    def find(self, alias):
        return self.__event_list.get(alias, None)
