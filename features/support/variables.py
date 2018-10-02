from .simple_result import SimpleResult


class Variables (object):
    def __init__(self):
        self.variables = {}

    def set_variable_result(self, variable, value):
        # Se necessario remove o $ no inicio do nome da variavel.
        if variable[0] == '$':
            variable = variable[1:]
        assert isinstance(value, SimpleResult)
        self.variables[variable] = value

    def get_variable_result(self, variable):
        if variable[0] == '$':
            variable = variable[1:]

        try:
            dot_position = variable.find('.')
            if dot_position == -1:
                struct = ""
                field_name = variable
                alias = ""
                return self.variables[field_name].get_result(alias)

            struct = variable[:dot_position]
            alias = variable[dot_position + 1:]

            return self.variables[struct].get_result(alias)
        except:
            message = "Variables: Erro ao tentar obter o conteudo da variavel.\n"
            message += "Variables: Variaveis definidas: %s\n" % self.variables.keys()
            message += "Variables: Tentando obter a variavel '%s': struct='%s' field='%s'.\n" % \
                (variable, struct, alias)
            assert False, message
