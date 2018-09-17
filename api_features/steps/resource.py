from behave import given, then, when

from api_features.support.utils import assert_equal


@given(u'que quero definir o recurso {resource_name}')  # noqa: F811
def step_impl(context, resource_name):
    context.resource = context.module.driver.add_resource(resource_name)


@given(u'os campos são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        alias = row['apelido']
        type = row['tipo']
        field = row['campo']
        location = row['localização']
        initial_value = row['valor']
        context.resource.add_field(alias, type, field, location, initial_value)


@given(u'os códigos de retorno são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        http_status_code = row['código']
        alias = row['status']
        context.resource.add_status_code_alias(int(http_status_code), alias)


@when(u'o evento é {event_name}')  # noqa: F811
def step_impl(context, event_name):
    context.event = context.resource.add_event(event_name)


@then(u'o método é {method}')  # noqa: F811
def step_impl(context, method):
    context.event.set_method(method)


@then(u'o path é {path}')  # noqa: F811
def step_impl(context, path):
    context.event.set_path(path)


@given(u'que quero {event}')  # noqa: F811
def step_impl(context, event):
    context.event = context.module.driver.find_event(event)
    context.resource = context.event.resource


@given(u'o campo {alias} é {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field = context.resource.get_field(alias)
    assert field is not None, 'Alias %s nao encontrado' % alias
    field_value = context.module.variables.get_content(field_value)
    field.set_value(field_value)
    # TODO: acho que os parameters (body) deveria ser montado na hora de enviar, como o header
    if field.location == 'body':
        context.event.parameters[field.json_name] = field.get_value()


@when(u'tento executar')  # noqa: F811
def step_impl(context):
    context.event.send()


@then(u'recebo o status {alias}')  # noqa: F811
def step_impl(context, alias):
    status = context.resource.get_status_code(alias)
    context.event.check_result(status.status_code)


@then(u'o campo {alias} tem o valor {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field = context.resource.get_field(alias)
    assert field is not None, 'Alias %s nao encontrado' % alias
    field_value = context.module.variables.get_content(field_value)
    assert_equal(context, context.event.result[field.json_name], field_value, "Valor do campo difere do esperado")
