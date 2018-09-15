from behave import given, then, when

from api_features.support.utils import assert_equal


@given(u'que quero definir o {event_name}')  # noqa: F811
def step_impl(context, event_name):
    context.event = context.module.driver.add_event(event_name)


@given(u'o path é {path}')  # noqa: F811
def step_impl(context, path):
    context.event.set_path(path)


@given(u'o método é {method}')  # noqa: F811
def step_impl(context, method):
    context.event.set_method(method)


@then(u'os campos são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        name = row['nome']
        type = row['tipo']
        field = row['campo no json']
        context.event.add_field(name, type, field)


@then(u'os códigos de retorno são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        http_status_code = row['código']
        alias = row['status']
        context.event.add_status_code_alias(int(http_status_code), alias)


@given(u'que quero {event}')  # noqa: F811
@given(u'que quero {event}')
def step_impl(context, event):
    context.event = context.module.driver.get_event(event)


@given(u'o campo {alias} é {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field = context.event.get_field(alias)
    assert field is not None, 'Alias %s nao encontrado' % alias
    field_value = context.module.variables.get_content(field_value)
    field.set_value(field_value)
    context.event.parameters[field.json_name] = field.get_value()


@when(u'tento executar')  # noqa: F811
def step_impl(context):
    context.event.send()


@then(u'recebo o status {alias}')  # noqa: F811
def step_impl(context, alias):
    status = context.event.get_status_code(alias)
    context.event.check_result(status.status_code)


@then(u'o campo {alias} tem o valor {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field = context.event.get_field(alias)
    assert field is not None, 'Alias %s nao encontrado' % alias
    field_value = context.module.variables.get_content(field_value)
    assert_equal(context, context.event.result[field.json_name], field_value, "Valor do campo difere do esperado")
