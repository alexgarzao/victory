import sqlite3


class Sqlite:
    connection_pool = {}

    def __init__(self):
        self.database_filename = ''
        self.sql = ''
        self.field_name = ''

    def query(self):
        conn = self.__get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sql)
        rows = cursor.fetchall()
        cursor.close()
        assert len(rows) == 1
        row = rows[0]

        if self.field_name:
            return row[self.field_name]

        assert len(row.keys()) == 1
        return row[0]

    def run(self, sql):
        conn = self.__get_connection()
        cursor = conn.cursor()
        cursor.executescript(sql)
        conn.commit()
        cursor.close()

    def __get_connection(self):
        conn_key = self.database_filename
        conn = Sqlite.connection_pool.get(conn_key, None)
        if conn == None:
            conn = sqlite3.connect(self.database_filename)
            conn.row_factory = sqlite3.Row
            Sqlite.connection_pool[conn_key] = conn

        return conn
