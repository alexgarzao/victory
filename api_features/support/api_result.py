from features.support.content_result import ContentResult
from features.support.simple_result import SimpleResult


class ApiResult(ContentResult):
    def __init__(self, context, json):
        self.context = context
        self.json = json

    def get_result(self, alias):
        field = self.context.resource.get_field(alias)
        if field:
            field_name = field.json_name
            return SimpleResult(self.json[field_name])

        raise Exception("ApiResult: Alias {} nao encontrado".format(alias))
