from behave import step


@step(u'que imprimo {message}')  # noqa: F811
def step_impl(context, message):
    print("*** Message: {} ***".format(message))
