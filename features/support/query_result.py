class QueryResult:
    def __init__(self, json):
        self.json = json

    def get_value(self, context, field_name):
        return self.json[field_name]
