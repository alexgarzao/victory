from nose.tools import *
from custom_asserts import *

from web_app import *


def test_valid_elements_in_one_screen():
    w = WebApp()
    s = w.new_screen('Screen A')
    s.add_id_element('X', 'X1')


@raises(DuplicatedElementException)
def test_dont_accept_duplicated_elements():
    w = WebApp()
    s = w.new_screen('Screen A')
    s.add_id_element('X', 'X1')
    s.add_xpath_element('X', 'X2')


def test_same_elements_in_two_screens():
    w = WebApp()
    s = w.new_screen('Screen A')
    s.add_id_element('X1', 'Y1')

    s = w.new_screen('Screen B')
    s.add_id_element('X1', 'Y1')


@raises(DuplicatedScreenException)
def test_avoid_duplicated_screens():
    w = WebApp()
    w.new_screen('Screen A')
    w.new_screen('Screen A')


@raises(DuplicatedScreenException)
def test_avoid_duplicated_screens():
    w = WebApp()
    w.new_screen('Screen A')
    w.new_screen('Screen A')


@raises(ScreenNotFoundException)
def test_avoid_undefined_screens_in_open():
    w = WebApp()
    w.new_screen('Screen A')
    w.open_screen('Screen B')


@raises(ScreenNotFoundException)
def test_avoid_undefined_screens_in_assert_screen_equal():
    w = WebApp()
    w.new_screen('Screen A')
    w.screen_assert_equal('Screen B')


def test_message_in_screen_not_found_exception():
    w = WebApp()
    w.new_screen('Screen A')
    assert_exception_and_message(
            ScreenNotFoundException,
            lambda: w.screen_assert_equal('Screen B'),
            'Screen Screen B not found. Possible values: Screen A',
    )


@raises(ElementNotFoundException)
def test_element_not_found():
    w = WebApp()
    s = w.new_screen('Screen A')
    s.add_id_element('X', 'X1')
    s.find_element('Y')


def test_message_in_element_not_found_exception():
    w = WebApp()
    s = w.new_screen('Screen A')
    s.add_id_element('X', 'X1')

    assert_exception_and_message(
            ElementNotFoundException,
            lambda: s.find_element('Y'),
            'Element Y not found. Possible values: X',
    )
