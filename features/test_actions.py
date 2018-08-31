from nose.tools import raises
from custom_asserts import assert_exception_and_message

from actions import Actions, DuplicatedActionException, UndefinedActionException


def test_action_with_one_event():
    a = Actions()
    assert a.get_action('A1') is None
    a.new_action('A1')
    a.add_event('A1', 'E1')
    assert a.get_action('A1') is not None


@raises(DuplicatedActionException)
def test_dont_accept_duplicated_actions():
    a = Actions()
    a.new_action('A1')
    a.add_event('A1', 'E1')
    a.new_action('A1')


def test_message_in_duplicated_action_exception():
    a = Actions()
    a.new_action('A1')
    a.add_event('A1', 'E1')

    assert_exception_and_message(
            DuplicatedActionException,
            lambda: a.new_action('A1'),
            'Action A1 already exists',
    )


def test_add_event_in_undefined_action():
    a = Actions()
    a.new_action('A1')

    assert_exception_and_message(
            UndefinedActionException,
            lambda: a.add_event('A2', 'E1'),
            'Undefined action A2. Possible values: A1',
    )


def test_run_undefined_action():
    a = Actions()
    assert a.get_action('A1') is None
    a.new_action('A1')
    a.add_event('A1', 'E1')

    assert_exception_and_message(
            UndefinedActionException,
            lambda: a.run_action(None, 'A2'),
            'Undefined action A2. Possible values: A1',
    )
