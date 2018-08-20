from sqlite import Sqlite


def test_create_example_database():
    q = Sqlite()
    q.database_filename = ':memory:'
    q.run("""
        drop table if exists dictionary;
        create table dictionary
                    (id smallint, word text);
        insert into dictionary
                    values (1, 'XXX10');
        insert into dictionary
                    values (2, 'XXX20');
        """)


def test_query_with_many_fields():
    q = Sqlite()
    q.database_filename = ':memory:'
    q.sql = """
      SELECT *
          FROM dictionary
          WHERE id = 1
    """
    q.field_name = 'word'
    assert q.query() == 'XXX10'


def test_query_with_one_field():
    q = Sqlite()
    q.database_filename = ':memory:'
    q.sql = """
      SELECT word
          FROM dictionary
          WHERE id = 1
    """
    assert q.query() == 'XXX10'
