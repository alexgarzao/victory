from behave import given, when, then


@given(u'que quero definir variáveis')  # noqa: F811
def step_impl(context):
    pass


@given(u'que quero consultar o valor de {variable}')  # noqa: F811
def step_impl(context, variable):
    context.variable_result = context.module.variables.get_variable_result(variable)


@then(u'defino que {variable} igual a {value}')  # noqa: F811
@when(u'defino que {variable} igual a {value}')  # noqa: F811
def step_impl(context, variable, value):
    context.module.variables.set_variable_result(variable, value)


@then(u'obtenho {valor_esperado_variavel}')  # noqa: F811
def step_impl(context, valor_esperado_variavel):
    valor_variavel = context.variable_result
    assert valor_variavel == valor_esperado_variavel, \
        "O resultado esperado [%s] e diferente do retorno [%s]." % (valor_esperado_variavel, valor_variavel)


# @then(u'eu salvo o resultado em {variavel}')  # noqa: F811
# def step_impl(context, variavel):
#     assert context.module.api.success()
#     context.module.variables.set_variable_result(variavel, context.module.api.retorno.json())
