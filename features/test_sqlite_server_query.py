import sqlite3

from queries import SqliteQuery


def __create_example_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''drop table if exists dictionary''')
    c.execute('''create table dictionary
                    (id smallint, word text)''')
    c.execute("""insert into dictionary
                    values (1, 'XXX10')""")
    c.execute("""insert into dictionary
                    values (2, 'XXX20')""")
    conn.commit()
    c.close()


def test_query_with_many_fields():
    __create_example_database()

    q = SqliteQuery()
    q.database_filename = 'example.db'
    q.sql = """
      SELECT *
          FROM dictionary
          WHERE id = 1
    """
    q.field_name = 'word'
    assert q.run() == 'XXX10'


def test_query_with_one_field():
    q = SqliteQuery()
    q.database_filename = 'example.db'
    q.sql = """
      SELECT word
          FROM dictionary
          WHERE id = 1
    """
    assert q.run() == 'XXX10'
