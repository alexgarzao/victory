from behave import given, then, when


@given(u'que quero definir o {action_name}')  # noqa: F811
def step_impl(context, action_name):
    context.action = context.module.driver.add_action(action_name)


@given(u'o path é {path}')  # noqa: F811
def step_impl(context, path):
    context.action.set_path(path)


@given(u'o método é {method}')  # noqa: F811
def step_impl(context, method):
    context.action.set_method(method)


@then(u'os campos são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        name = row['nome']
        type = row['tipo']
        field = row['campo no json']
        context.action.add_field(name, type, field)


@then(u'os códigos de retorno são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        http_status_code = row['código']
        alias = row['status']
        context.action.add_status_code_alias(int(http_status_code), alias)


@given(u'que quero {action}')  # noqa: F811
@given(u'que quero {action}')
def step_impl(context, action):
    context.action = context.module.driver.get_action(action)


@given(u'o campo {alias} é {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field = context.action.get_field(alias)
    assert field is not None, 'Alias %s nao encontrado' % alias
    field.set_value(field_value)
    context.action.parameters[field.json_name] = field.get_value()


@when(u'tento executar')  # noqa: F811
def step_impl(context):
    context.action.send()


@then(u'recebo o status {alias}')  # noqa: F811
def step_impl(context, alias):
    status = context.action.get_status_code(alias)
    context.action.check_result(status.status_code)
