import pyodbc

from features.support.simple_result import SimpleResult
from features.support.query_result import QueryResult


class SqlServer:
    connection_pool = {}

    def __init__(self):
        self.server_address = ''
        self.username = ''
        self.user_password = ''
        self.database_name = ''
        self.sql = ''
        self.field_name = ''

    def query(self, field_name=''):
        if not field_name:
            field_name = self.field_name

        conn = self.__get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sql)
        rows = cursor.fetchall()
        cursor.close()
        assert len(rows) == 1
        row = rows[0]

        if field_name:
            return SimpleResult(row.__getattribute__(field_name))

        return QueryResult(row)

    def run(self, sql):
        conn = self.__get_connection()
        cursor = conn.cursor()
        cursor.executescript(sql)
        conn.commit()
        cursor.close()

    def __get_connection(self):
        conn_key = self.server_address + '|' + self.database_name + '|' + self.username + '|' + self.user_password
        conn = SqlServer.connection_pool.get(conn_key, None)
        if conn is None:
            conn = pyodbc.connect(
                    driver='{ODBC Driver 17 for SQL Server}',
                    server=self.server_address,
                    database=self.database_name,
                    uid=self.username,
                    pwd=self.user_password,
            )

            SqlServer.connection_pool[conn_key] = conn

        return conn
