import sqlite3


class SqliteQuery:
    def __init__(self):
        self.database_filename = ''
        self.sql = ''
        self.field_name = ''

    def run(self):
        conn = sqlite3.connect(self.database_filename)
        conn.row_factory = sqlite3.Row
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
