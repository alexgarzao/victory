import pyodbc


class Queries:
    def __init__(self):
        self.queries = {}

    def add(self, name):
        new_query = Query(name)
        self.queries[name] = new_query
        return new_query

    def run(self, name):
        query = self.queries[name]
        return query.run()


class Query:
    def __init__(self, name):
        self.name = name
        self.server_address = ''
        self.username = ''
        self.user_password = ''
        self.database_name = ''
        self.sql = ''
        self.field_name = ''

    def run(self):
        conn = pyodbc.connect(
                driver = '{ODBC Driver 17 for SQL Server}',
                server = self.server_address,
                database = self.database_name,
                uid=self.username,
                pwd=self.user_password,
        )

        cursor = conn.cursor()
        cursor.execute(self.sql)
        rows = cursor.fetchall()
        assert len(rows) == 1
        row = rows[0]

        if self.field_name:
            return row.__getattribute__(self.field_name)

        assert len(row.cursor_description) == 1
        return row[0]
