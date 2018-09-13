from behave import step


@step(u'a ação {action_name} é')  # noqa: F811
def step_impl(context, action_name):
    context.driver.get_current_screen().add_action(action_name)

    for row in context.table:
        context.driver.get_current_screen().add_event_in_action(action_name, event=row['evento'])


@step(u'executo a {action_name}')  # noqa: F811
@step(u'executo o {action_name}')
def step_impl(context, action_name):
    steps_to_execute = context.driver.get_current_screen().get_steps_to_execute(action_name)
    context.execute_steps(steps_to_execute)
