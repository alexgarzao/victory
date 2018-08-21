from sqlite import Sqlite
from sqlserver import SqlServer


class Queries:
    def __init__(self):
        self.query_list = {}

    def add(self, db_type, name):
        if db_type == 'SQLITE':
            query = Sqlite()
        elif db_type == 'SQLSERVER':
            query = SqlServer()
        else:
            raise InvalidDbTypeException("Invalid DB Type: {}. Possible values: SQLITE, SQLSERVER.".format(db_type))

        if self.query_list.get(name) != None:
            raise DuplicatedQueryException("Query {} already exists".format(name))

        self.query_list[name] = query
        return query

    def run(self, name):
        query = self.query_list.get(name)
        if not query:
            possible = ','.join(list(self.query_list))
            raise NotFoundQueryException("Query {} not found. Possible values: {}".format(name, possible))

        return query.query()


class InvalidDbTypeException(Exception):
    pass


class DuplicatedQueryException(Exception):
    pass


class NotFoundQueryException(Exception):
    pass
