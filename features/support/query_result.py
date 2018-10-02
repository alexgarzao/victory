from .content_result import ContentResult
from features.support.simple_result import SimpleResult


class QueryResult(ContentResult):
    def __init__(self, json):
        self.json = json

    def get_result(self, field_name):
        return SimpleResult(self.json[field_name])
