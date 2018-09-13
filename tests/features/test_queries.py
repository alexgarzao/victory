from nose.tools import raises, assert_raises, assert_equal

from .context import Queries, InvalidDbTypeException, DuplicatedQueryException, NotFoundQueryException


def test_accept_valid_db_types():
    q = Queries()
    q.add('SQLITE', 'Q1')
    q.add('SQLSERVER', 'Q2')


def test_accept_valid_db_types_case_insensitive():
    q = Queries()
    q.add('SQLite', 'Q1')
    q.add('SQLServer', 'Q2')


@raises(InvalidDbTypeException)
def test_dont_accept_invalid_db_types():
    q = Queries()
    q.add('SQLX', 'Q1')


@raises(DuplicatedQueryException)
def test_dont_accept_duplicated_queries():
    q = Queries()
    q.add('SQLITE', 'Q1')
    q.add('SQLSERVER', 'Q1')


@raises(DuplicatedQueryException)
def test_dont_accept_duplicated_queries_case_insensitive():
    q = Queries()
    q.add('SQLITE', 'Q1')
    q.add('SQLSERVER', 'q1')


@raises(NotFoundQueryException)
def test_query_an_invalid_query():
    q = Queries()
    q.add('SQLITE', 'Q1')
    q.run('Q2')


def test_query_an_invalid_query_and_show_possibilities():
    q = Queries()
    q.add('SQLITE', 'Q1')

    with assert_raises(NotFoundQueryException) as cm:
        q.run('Q2')

    the_exception = cm.exception
    the_message = the_exception.args[0]
    assert_equal(the_message, 'Query q2 not found. Possible values: q1')
