from sqlite_query import SqliteQuery
from sqlserver_query import SqlServerQuery


class Queries:
    def __init__(self):
        self.queries = {}

    def add(self, db_type, name):
        if db_type == 'SQLITE':
            new_query = SqliteQuery()
        elif db_type == 'SQLSERVER':
            new_query = SqlServerQuery()
        else:
            assert False

        self.queries[name] = new_query
        return new_query

    def run(self, name):
        query = self.queries[name]
        return query.run()
