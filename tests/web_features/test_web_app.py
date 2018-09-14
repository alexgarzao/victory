from nose.tools import raises

from .context import assert_exception_and_message
from .context import WebDriver
from .context import DuplicatedScreenException, ScreenNotFoundException
from .context import DuplicatedElementException, ElementNotFoundException


def test_valid_elements_in_one_screen():
    w = WebDriver()
    s = w.add_screen('Screen A')
    s.add_id_element('X', 'X1')


@raises(DuplicatedElementException)
def test_dont_accept_duplicated_elements():
    w = WebDriver()
    s = w.add_screen('Screen A')
    s.add_id_element('X', 'X1')
    s.add_xpath_element('X', 'X2')


def test_same_elements_in_two_screens():
    w = WebDriver()
    s = w.add_screen('Screen A')
    s.add_id_element('X1', 'Y1')

    s = w.add_screen('Screen B')
    s.add_id_element('X1', 'Y1')


@raises(DuplicatedScreenException)
def test_avoid_duplicated_screens():
    w = WebDriver()
    w.add_screen('Screen A')
    w.add_screen('Screen A')


@raises(ScreenNotFoundException)
def test_avoid_undefined_screens_in_open():
    w = WebDriver()
    w.add_screen('Screen A')
    w.open_screen('Screen B')


@raises(ScreenNotFoundException)
def test_avoid_undefined_screens_in_assert_screen_equal():
    w = WebDriver()
    w.add_screen('Screen A')
    w.screen_assert_equal('Screen B')


def test_message_in_screen_not_found_exception():
    w = WebDriver()
    w.add_screen('Screen A')
    assert_exception_and_message(
            ScreenNotFoundException,
            lambda: w.screen_assert_equal('Screen B'),
            'Screen screen b not found. Possible values: screen a',
    )


@raises(ElementNotFoundException)
def test_element_not_found():
    w = WebDriver()
    s = w.add_screen('Screen A')
    s.add_id_element('X', 'X1')
    s.find_element('Y')


def test_message_in_element_not_found_exception():
    w = WebDriver()
    s = w.add_screen('Screen A')
    s.add_id_element('X', 'X1')

    assert_exception_and_message(
            ElementNotFoundException,
            lambda: s.find_element('Y'),
            'Element y not found. Possible values: x',
    )
