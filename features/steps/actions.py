from behave import step


@step(u'a ação {action_name} é')  # noqa: F811
def step_impl(context, action_name):
    context.driver.new_action(action_name)

    for row in context.table:
        context.driver.add_event_in_action(action_name, event=row['evento'])


@step(u'executo a {action_name}')  # noqa: F811
@step(u'executo o {action_name}')
def step_impl(context, action_name):
    context.driver.run_action(context, action_name)
