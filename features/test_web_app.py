from nose.tools import *

from web_app import *


def test_valid_elements_in_one_screen():
    w = WebApp()
    w.set_current_screen('Screen A')
    w.new_id_element('X', 'X1')


@raises(DuplicatedElementException)
def test_dont_accept_duplicated_elements():
    w = WebApp()
    w.set_current_screen('Screen A')
    w.new_id_element('X', 'X1')
    w.new_xpath_element('X', 'X2')


def test_same_elements_in_two_screens():
    w = WebApp()
    w.set_current_screen('Screen A')
    w.new_id_element('X1', 'Y1')

    w.set_current_screen('Screen B')
    w.new_id_element('X1', 'Y1')


@raises(DuplicatedScreenException)
def test_avoid_duplicated_screens():
    w = WebApp()
    w.new_screen('Screen A', 'URL A')
    w.new_screen('Screen A', 'URL X')
