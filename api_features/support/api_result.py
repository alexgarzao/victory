class ApiResult:
    def __init__(self, json):
        self.json = json

    def get_value(self, context, alias):
        field = context.resource.get_field(alias)
        if field:
            field_name = field.json_name
            return self.json[field_name]

        raise Exception("ApiResult: Alias {} nao encontrado".format(alias))
