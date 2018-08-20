from nose.tools import *

from queries import *


def test_accept_valid_db_types():
    q = Queries()
    q.add('SQLITE', 'Q1')
    q.add('SQLSERVER', 'Q2')


@raises(InvalidDbTypeException)
def test_dont_accept_invalid_db_types():
    q = Queries()
    q.add('SQLX', 'Q1')


@raises(DuplicatedQueryException)
def test_dont_accept_duplicated_queries():
    q = Queries()
    q.add('SQLITE', 'Q1')
    q.add('SQLSERVER', 'Q1')


@raises(NotFoundQueryException)
def test_query_an_invalid_query():
    q = Queries()
    q.add('SQLITE', 'Q1')
    q.run('Q2')
