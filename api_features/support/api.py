import json
import requests
from .utils import pretty_json


# TODO: Ou Request?
class Api(object):
    def __init__(self, headers, parameters, body):
        self.__headers = headers
        self.__parameters = parameters
        self.__body = body

    def set_field_value(self, name, location, value):
        if location == 'header':
            self.__headers[name] = value
        elif location == 'path':
            self.__parameters[name] = value
        elif location == 'body':
            self.__body[name] = value
        else:
            assert False, "Undefined location {}!".format(location)

    def get_parameters(self):
        return self.__parameters

    def get(self, url):
        try:
            self.url = url
            self.retorno = requests.get(self.url, headers=self.__headers)
            return self.retorno
        except Exception as e:
            raise e

    def post(self, url):
        try:
            self.url = url
            self.retorno = requests.post(self.url, headers=self.__headers, json=self.__body)
            return self.retorno
        except Exception as e:
            raise e

    def put(self, url):
        try:
            self.url = url
            self.retorno = requests.put(self.url, headers=self.__headers, json=self.__body)
            return self.retorno
        except Exception as e:
            raise e

    def delete(self, url):
        try:
            self.url = url
            self.retorno = requests.delete(self.url, headers=self.__headers, json=self.__body)
            return self.retorno
        except Exception as e:
            raise e

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
        json_enviado = json.dumps(self.__parameters, indent=4, sort_keys=True, separators=(',', ': '))
        if self.retorno.status_code >= 200 and self.retorno.status_code <= 201 and self.retorno.text:
            json_recebido = json.dumps(self.retorno.json(), indent=4, sort_keys=True, separators=(',', ': '))
        else:
            json_recebido = self.retorno.text
        assert self.retorno.status_code == retorno_esperado, \
            "O resultado esperado [{}] e diferente do retorno [{}].\n\tURL={}\n\tParametros enviados={}\n\tRetorno={}".\
            format(retorno_esperado, self.retorno.status_code, self.url, json_enviado, json_recebido)

        self._verify_error_response(self.retorno)

    def success(self):
        return self.retorno.status_code >= 200 and self.retorno.status_code <= 204

    def assert_result(self, field_name, expected_result):
        json_enviado = json.dumps(self.__parameters, indent=4, sort_keys=True, separators=(',', ': '))
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
