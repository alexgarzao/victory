class HttpStatusCodeAlias(object):
    def __init__(self, status_code, alias):
        self.status_code = status_code
        self.alias = alias


class HttpStatusCodeAliasList(object):
    def __init__(self):
        self.__http_status_code_alias_list = {}

    def add(self, status_code, alias):
        self.__http_status_code_alias_list[alias] = HttpStatusCodeAlias(status_code, alias)

    def get(self, alias):
        return self.__http_status_code_alias_list[alias]

    def get_code(self, alias):
        return self.__http_status_code_alias_list[alias].status_code
