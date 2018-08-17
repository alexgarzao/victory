from sqlite import Sqlite
from sqlserver import SqlServer


class Queries:
    def __init__(self):
        self.dbms_list = {}

    def add(self, db_type, name):
        if db_type == 'SQLITE':
            dbms = Sqlite()
        elif db_type == 'SQLSERVER':
            dbms = SqlServer()
        else:
            assert False

        self.dbms_list[name] = dbms
        return dbms

    def run(self, name):
        dbms = self.dbms_list[name]
        return dbms.query()
