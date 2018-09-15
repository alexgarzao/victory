class Variables (object):
    def __init__(self, context):
        self.variables = {}
        self.context = context

    def set_variable_result(self, variable, value):
        # Se necessario remove o $ no inicio do nome da variavel.
        if variable[0] == '$':
            variable = variable[1:]
        self.variables[variable] = value

    def get_variable_result(self, variable):
        try:
            dot_position = variable.find('.')
            if dot_position == -1:
                struct = ""
                field = variable
                return self.variables[field]

            struct = variable[:dot_position]
            alias = variable[dot_position + 1:]
            field = self.context.action.get_field(alias).json_name
            return self.variables[struct][field]
        except:
            message = "Variables: Erro ao tentar obter o conteudo da variavel.\n"
            message += "Variables: Variaveis definidas: %s\n" % self.variables.keys()
            message += "Variables: Tentando obter a variavel '%s': struct='%s' field='%s'.\n" % \
                (variable, struct, alias)
            assert False, message

    def get_content(self, content):
        if type(content) == str and content and content[0] == '$':
            return self.get_variable_result(content[1:])

        return content
