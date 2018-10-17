from enum import IntEnum, unique


from .utils import is_float


@unique
class FieldType(IntEnum):
    STRING = 1
    INTEGER = 2
    NUMBER = 3
    BOOL = 4
    DATE = 5
    STRING_LIST = 6
    INTEGER_LIST = 7


# REFACTOR: Esta classe poderia se especializada conforme o tipo.
# Assim poderiamos remover os if's abaixo.
class Field(object):
    def __init__(self, alias, type, json_name, location, initial_value):
        self.alias = alias
        self.type = FieldType[type.upper()]
        self.json_name = json_name
        self.location = location
        self.initial_value = None
        self.has_initial_value = False

        if initial_value != "":
            self.initial_value = self.transform_value(initial_value)
            self.has_initial_value = True

    def transform_value(self, value):
        if self.type == FieldType.STRING:
            return self.__get_string_value(value)
        elif self.type == FieldType.INTEGER:
            return self.__get_integer_value(value)
        elif self.type == FieldType.NUMBER:
            return self.__get_number_value(value)
        elif self.type == FieldType.BOOL:
            return self.__get_bool_value(value)
        elif self.type == FieldType.STRING_LIST:
            if value:
                return self.__get_string_list_value(value)
            else:
                return None
        elif self.type == FieldType.DATE:
            return self.__get_date_value(value)
        else:
            assert False, 'FieldType {} indefinido!'.format(self.type)

    def __get_string_value(self, value):
        # Verifica se tem " ou ' para serem retirados
        if len(value) >= 2:
            if value[0] == '\'' and value[len(value)-1] == '\'' or \
                    value[0] == '"' and value[len(value)-1] == '"':
                value = value[1:-1]
        return value

    def __get_integer_value(self, value):
        if value == '<nulo>':
            return None

        if type(value) is str and value.isdigit():
            return int(value)

        return value

    def __get_number_value(self, value):
        if value == '<nulo>':
            return None

        if type(value) is str and is_float(value):
            return float(value)

        return value

    def __get_bool_value(self, value):
        if value == '<nulo>':
            return None

        return value.upper() == 'SIM'

    def __get_string_list_value(self, value):
        if value == '<vazio>':
            return []

        if value == '<nulo>':
            return None

        return value.split(',')

    def __get_date_value(self, value):
        return value  # TODO: correto???


class Fields(object):
    def __init__(self):
        self.__field_list_by_alias = {}
        self.__field_list_by_name = {}

    def add(self, name, type, json_name, location, initial_value):
        field = Field(name, type, json_name, location, initial_value)
        self.__field_list_by_alias[name] = field
        self.__field_list_by_name[json_name] = field

    def get(self, alias):
        return self.__field_list_by_alias.get(alias)

    def get_by_name(self, name):
        return self.__field_list_by_name.get(name)

    def get_fields_in(self, location):
        return {alias: self.__field_list_by_alias[alias] for alias in self.__field_list_by_alias if self.__field_list_by_alias[alias].location == location}
