from behave import *

from sqlite import Sqlite


@given(u'que crio um banco para testar a execução de queries')
def step_impl(context):
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
