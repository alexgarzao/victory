from .sqlite import Sqlite
from .sqlserver import SqlServer


class Queries:
    def __init__(self):
        self.query_list = {}

    def add(self, db_type, name):
        db_type = db_type.upper()
        name = name.lower()
        if db_type == 'SQLITE':
            query = Sqlite()
        elif db_type == 'SQLSERVER':
            query = SqlServer()
        else:
            raise InvalidDbTypeException("Invalid DB Type: {}. Possible values: SQLITE, SQLSERVER.".format(db_type))

        if self.query_list.get(name) is not None:
            raise DuplicatedQueryException("Query {} already exists".format(name))

        self.query_list[name] = query
        return query

    def run(self, name):
        name = name.lower()
        query_name, field_name = self.__split(name)
        query = self.query_list.get(query_name)
        if not query:
            possible = ','.join(list(self.query_list))
            raise NotFoundQueryException("Query {} not found. Possible values: {}".format(name, possible))

        return query.query(field_name)

    def __split(self, name):
        split = name.split('.')
        if len(split) == 1:
            return name, ''

        return split[0], split[1]


class InvalidDbTypeException(Exception):
    pass


class DuplicatedQueryException(Exception):
    pass


class NotFoundQueryException(Exception):
    pass
