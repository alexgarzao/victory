from behave import given, then, when
from hamcrest import assert_that

from api_features.support.utils import assert_equal
from api_features.support.api_result import ApiResult


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
    context.request = context.event.get_new_request()
    context.resource = context.event.resource


@given(u'o campo {alias} é {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field_value = context.module.get_content(field_value).get_value()
    context.request.set_field_value(alias, field_value)


@when(u'tento executar')  # noqa: F811
def step_impl(context):
    context.request.send()


@then(u'recebo o status {alias}')  # noqa: F811
def step_impl(context, alias):
    status = context.resource.get_status_code(alias)
    context.request.check_result(status.status_code)


@then(u'o campo {alias} tem o valor {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field = context.resource.get_field(alias)
    assert_that(field is not None, 'Alias %s nao encontrado' % alias)
    field_value = context.module.get_content(field_value).get_value()
    assert_equal(context, context.request.result[field.json_name], field_value, "Valor do campo difere do esperado")


@then(u'salvo o resultado em {variable}')  # noqa: F811
def step_impl(context, variable):
    assert context.request.success()
    context.module.set_variable_result(variable, ApiResult(context, context.request.retorno.json()))
