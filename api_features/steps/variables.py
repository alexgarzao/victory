from behave import given, when, then


@given(u'que eu quero obter o resultado de uma variável')  # noqa: F811
def step_impl(context):
    pass


@when(u'eu obtenho o resultado da variável {variavel}')  # noqa: F811
def step_impl(context, variavel):
    context.variable_result = context.config.variables.get_variable_result(variavel)


@then(u'eu obtenho o valor {valor_esperado_variavel}')  # noqa: F811
def step_impl(context, valor_esperado_variavel):
    valor_variavel = context.variable_result
    assert valor_variavel == valor_esperado_variavel, \
        "O resultado esperado [%s] e diferente do retorno [%s]." % (valor_esperado_variavel, valor_variavel)


@then(u'eu salvo o resultado em {variavel}')  # noqa: F811
def step_impl(context, variavel):
    assert context.api.success()
    context.config.variables.set_variable_result(variavel, context.api.retorno.json())
