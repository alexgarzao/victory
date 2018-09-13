from nose.tools import raises

from .context import assert_exception_and_message

from .context import Actions, DuplicatedActionException, UndefinedActionException


def test_action_with_one_event():
    a = Actions()
    assert a.get_action('A1') is None
    a.add_action('A1')
    a.add_event('A1', 'E1')
    assert a.get_action('A1') is not None


def test_action_with_one_event_case_insensitive():
    a = Actions()
    assert a.get_action('A1') is None
    a.add_action('A1')
    a.add_event('A1', 'E1')
    assert a.get_action('a1') is not None


@raises(DuplicatedActionException)
def test_dont_accept_duplicated_actions():
    a = Actions()
    a.add_action('A1')
    a.add_event('A1', 'E1')
    a.add_action('A1')


@raises(DuplicatedActionException)
def test_dont_accept_duplicated_actions_case_insensitive():
    a = Actions()
    a.add_action('A1')
    a.add_event('A1', 'E1')
    a.add_action('a1')


def test_message_in_duplicated_action_exception():
    a = Actions()
    a.add_action('A1')
    a.add_event('A1', 'E1')

    assert_exception_and_message(
            DuplicatedActionException,
            lambda: a.add_action('A1'),
            'Action a1 already exists',
    )


def test_add_event_in_undefined_action():
    a = Actions()
    a.add_action('A1')

    assert_exception_and_message(
            UndefinedActionException,
            lambda: a.add_event('A2', 'E1'),
            'Undefined action a2. Possible values: a1',
    )


def test_run_undefined_action():
    a = Actions()
    assert a.get_action('A1') is None
    a.add_action('A1')
    a.add_event('A1', 'E1')

    assert_exception_and_message(
            UndefinedActionException,
            lambda: a.run_action(None, 'A2'),
            'Undefined action A2. Possible values: a1',
    )
