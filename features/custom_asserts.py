from nose.tools import *


def assert_exception_and_message(exception_class, function, expected_message):
    with assert_raises(exception_class) as cm:
        function()

    the_exception = cm.exception
    the_message = str(the_exception)
    assert_equal(the_message, expected_message)
