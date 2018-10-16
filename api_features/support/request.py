import json
import requests
from .utils import pretty_json


class Request:
    def __init__(self, event):
        self.__event = event
        self.__resource = event.resource
        self._headers = self.__resource.get_initial_headers()
        self._parameters = self.__resource.get_initial_parameters()
        self._body = self.__resource.get_initial_body()

    def set_field_value(self, alias, value):
        field = self.__resource.get_field(alias)
        assert field is not None, 'Alias %s nao encontrado' % alias

        name = field.json_name
        value = field.transform_value(value)
        location = field.location

        if location == 'header':
            self._headers[name] = value
        elif location == 'path':
            self._parameters[name] = value
        elif location == 'body':
            self._body[name] = value
        else:
            assert False, "Undefined location {}!".format(location)

    def add_table_field_list(self, object_name, table_field_list):
        rows_to_add = []

        for row in table_field_list.rows:
            fields_to_add = {}

            for alias, value in row.items():
                field = self.__resource.get_field(alias)
                assert field is not None, 'Alias %s nao encontrado' % alias

                name = field.json_name
                value = field.transform_value(value)
                location = field.location

                assert location == "body", "Location {} is invalid. Only body is accepted in arrays!".format(location)
                fields_to_add[name] = value

            rows_to_add.append(fields_to_add)

        self._body[object_name] = rows_to_add

    def _define_result(self):
        if self.retorno.status_code >= 200 and self.retorno.status_code <= 201 and self.retorno.text:
            self.result = self.retorno.json()
        else:
            self.result = {}

    def check_result(self, status_code):
        self.validar_retorno(status_code)

    def get_url(self):
        path = self.__replace_parameters(self.__event.path, self._parameters)
        return self.__resource.base_url + '/' + path

    def __replace_parameters(self, text, parameters):
        for parameter, value in parameters.items():
            if type(value) is not str and type(value) is not int:
                continue
            field = self.__resource.get_field_by_name(parameter)
            token_to_find = "{" + field.alias + "}"
            text = text.replace(token_to_find, str(value))

        return text

    # def post_image(self, caminho_imagem):
    #     try:
    #         url = self.url
    #         self.last_parameters = None
    #         self.retorno = requests.post(url, files={'file': open(caminho_imagem, 'rb')})
    #         return self.retorno
    #     except Exception as e:
    #         raise e
    #

    def validar_retorno(self, retorno_esperado):
        headers_sent = json.dumps(self._headers, indent=4, sort_keys=True, separators=(',', ': '))
        parameters_sent = json.dumps(self._parameters, indent=4, sort_keys=True, separators=(',', ': '))
        body_sent = json.dumps(self._body, indent=4, sort_keys=True, separators=(',', ': '))
        if self.retorno.status_code >= 200 and self.retorno.status_code <= 201 and self.retorno.text:
            json_recebido = json.dumps(self.retorno.json(), indent=4, sort_keys=True, separators=(',', ': '))
        else:
            json_recebido = self.retorno.text
        assert self.retorno.status_code == retorno_esperado, \
            "O resultado esperado [{}] e diferente do retorno [{}].\n\tURL={}\n\tHeaders enviados={}\n\tParametros enviados={}\n\tBody enviado={}\n\tRetorno={}".\
            format(retorno_esperado, self.retorno.status_code, self.url, headers_sent, parameters_sent, body_sent, json_recebido)

        self._verify_error_response(self.retorno)

    def success(self):
        return self.retorno.status_code >= 200 and self.retorno.status_code <= 204

    def assert_result(self, field_name, expected_result):
        json_enviado = json.dumps(self._parameters, indent=4, sort_keys=True, separators=(',', ': '))
        if self.retorno.status_code >= 200 and self.retorno.status_code <= 201:
            json_recebido = json.dumps(self.retorno.json(), indent=4, sort_keys=True, separators=(',', ': '))
        else:
            json_recebido = self.retorno.text
        result = self.retorno.json()[field_name]
        assert result == expected_result, \
            "O resultado esperado [%s] e diferente do retorno [%s].\n\tURL=%s\n\tParametros enviados=%s\n\tRetorno=%s" % (expected_result, result, self.url, json_enviado, json_recebido)

    def json_return_value(self, key):
        msg = 'Chave %s nao encontrada no retorno: %s' % (key, pretty_json(self.retorno.json()))
        assert key in self.retorno.json(), msg
        return self.retorno.json()[key]

    def _verify_error_response(self, api_response):
        """ Verifica a estrutura de retorno em caso de erro. """
        if api_response.status_code < 400 or api_response.status_code > 499:
            return

        try:
            api_response.json()
        except Exception as e:
            if api_response.status_code == 404:
                return


class GetRequest(Request):
    def __init__(self, event):
        super().__init__(event)

    def send(self):
        try:
            self.url = self.get_url()
            self.retorno = requests.get(self.url, headers=self._headers)
            self._define_result()
            return self.retorno
        except Exception as e:
            raise e


class PostRequest(Request):
    def __init__(self, event):
        super().__init__(event)

    def send(self):
        try:
            self.url = self.get_url()
            self.retorno = requests.post(self.url, headers=self._headers, json=self._body)
            self._define_result()
            return self.retorno
        except Exception as e:
            raise e


class PutRequest(Request):
    def __init__(self, event):
        super().__init__(event)

    def send(self):
        try:
            self.url = self.get_url()
            self.retorno = requests.put(self.url, headers=self._headers, json=self._body)
            self._define_result()
            return self.retorno
        except Exception as e:
            raise e


class DeleteRequest(Request):
    def __init__(self, event):
        super().__init__(event)

    def send(self):
        try:
            self.url = self.get_url()
            self.retorno = requests.delete(self.url, headers=self._headers, json=self._body)
            self._define_result()
            return self.retorno
        except Exception as e:
            raise e
