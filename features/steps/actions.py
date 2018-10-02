from behave import given, when, then


@then(u'a ação {action_name} é')  # noqa: F811
def step_impl(context, action_name):
    context.module.driver.get_current_screen().add_action(action_name)

    for row in context.table:
        context.module.driver.get_current_screen().add_event_in_action(action_name, event=row['evento'])


@when(u'executo a ação genérica {action_name}')  # noqa: F811
@then(u'executo a ação genérica {action_name}')
def step_impl(context, action_name):
    steps_to_execute = context.module.get_steps_to_execute(action_name)
    context.execute_steps(steps_to_execute)


@when(u'executo a {action_name}')  # noqa: F811
@when(u'executo o {action_name}')
@then(u'executo a {action_name}')
@then(u'executo o {action_name}')
def step_impl(context, action_name):
    steps_to_execute = context.module.driver.get_current_screen().get_steps_to_execute(action_name)
    context.execute_steps(steps_to_execute)


@given(u'que quero definir a ação {action_name}')  # noqa: F811
def step_impl(context, action_name):
    context.current_generic_action_name = action_name
    context.module.add_generic_action(action_name)


@then(u'a lista de eventos é')  # noqa: F811
def step_impl(context):
    for row in context.table:
        context.module.add_event_in_generic_action(context.current_generic_action_name, event=row['evento'])
