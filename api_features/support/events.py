from .api import Api


class Event(object):
    def __init__(self, resource):
        self.resource = resource
        self.path = None
        self.method = None

    def set_path(self, value):
        self.path = value

    def set_method(self, value):
        self.method = value

    def init(self):
        # TODO: acho que esse "init" seria uma nova classe (Request?) ou a API (talvez)
        # TODO: Talvez seria um metodo que retorna uma instancia de API/Request, e o send abaixo ficaria encapsulado nesta instancia
        # TODO: Talvez teriamos GetRequest, PostRequest, DeleteRequest, ...
        self.api = Api(self.__get_initial_headers(), self.__get_initial_parameters(), self.__get_initial_body())
        self.result = {}

    def set_field_value(self, alias, value):
        field = self.resource.get_field(alias)
        assert field is not None, 'Alias %s nao encontrado' % alias
        self.api.set_field_value(field.json_name, field.location, field.transform_value(value))

    def send(self):
        # print("Method: {}\nURL: {}\nParameters: {}\n".format(self.method, self.__get_url(), self.parameters))
        if self.method == 'POST':
            self.api.post(self.__get_url())
        elif self.method == 'GET':
            self.api.get(self.__get_url())
        elif self.method == 'PUT':
            self.api.put(self.__get_url())
        elif self.method == 'DELETE':
            self.api.delete(self.__get_url())
        else:
            assert False

        if self.api.retorno.status_code >= 200 and self.api.retorno.status_code <= 201 and self.api.retorno.text:
            self.result = self.api.retorno.json()
        else:
            self.result = {}

    def check_result(self, status_code):
        self.api.validar_retorno(status_code)

    def __get_url(self):
        path = self.__replace_parameters(self.path, self.api.get_parameters())
        return self.resource.base_url + '/' + path

    def __replace_parameters(self, text, parameters):
        for parameter, value in parameters.items():
            if type(value) is not str and type(value) is not int:
                continue
            field = self.resource.get_field_by_name(parameter)
            token_to_find = "{" + field.alias + "}"
            text = text.replace(token_to_find, str(value))

        return text

    def __get_initial_headers(self):
        return self.resource.get_initial_headers()

    def __get_initial_body(self):
        return self.resource.get_initial_body()

    def __get_initial_parameters(self):
        return self.resource.get_parameters()


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
