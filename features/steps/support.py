from behave import given, when, then


@given(u'que imprimo {message}')  # noqa: F811
@when(u'imprimo {message}')
@then(u'imprimo {message}')
def step_impl(context, message):
    print("*** Message: {} ***\n".format(message))
