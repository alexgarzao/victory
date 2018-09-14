from behave import given, then, when


@given(u'que quero definir o endpoint de {endpoint_name}')  # noqa: F811
def step_impl(context, endpoint_name):
    context.module.driver.add_endpoint(endpoint_name)


@given(u'o path é {path}')  # noqa: F811
def step_impl(context, path):
    # TODO: daria para guardar o current endpont em context... seria uma bao estrategia?
    context.module.driver.get_current_endpoint().set_path(path)


@given(u'o método é {method}')  # noqa: F811
def step_impl(context, method):
    context.module.driver.get_current_endpoint().set_method(method)


@then(u'os campos são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        name = row['nome']
        type = row['tipo']
        field = row['campo no json']
        context.module.driver.get_current_endpoint().add_field(name, type, field)


@then(u'os códigos de retorno são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        http_status_code = row['código']
        alias = row['status']
        context.module.driver.get_current_endpoint().add_status_code_alias(int(http_status_code), alias)


@given(u'que quero executar o {endpoint}')  # noqa: F811
@given(u'que quero executar a {endpoint}')
def step_impl(context, endpoint):
    context.endpoint = context.module.driver.get_endpoint(endpoint)


@given(u'o campo {alias} é {field_value}')  # noqa: F811
def step_impl(context, alias, field_value):
    field = context.endpoint.get_field(alias)
    assert field is not None, 'Alias %s nao encontrado' % alias
    field.set_value(field_value)
    context.endpoint.parameters[field.json_name] = field.get_value()


@when(u'tento executar')  # noqa: F811
def step_impl(context):
    context.endpoint.send()


@then(u'recebo o status {alias}')  # noqa: F811
def step_impl(context, alias):
    status = context.endpoint.get_status_code(alias)
    context.endpoint.check_result(status.status_code)
