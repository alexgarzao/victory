from behave import given, when, then

from api_features.support.utils import assert_equal


@given(u'que quero consultar o valor de {variable}')  # noqa: F811
@when(u'consulto o valor de {variable}')
def step_impl(context, variable):
    context.variable_result = context.module.get_content("$var:" + variable).get_value()


@given(u'que {variable} igual a {value}')  # noqa: F811
@then(u'defino que {variable} igual a {value}')
@when(u'defino que {variable} igual a {value}')
@given(u'que {variable} = {value}')
def step_impl(context, variable, value):
    value = context.module.get_content(value)
    context.module.set_variable_result(variable, value)


@then(u'obtenho o valor {expected_value}')  # noqa: F811
def step_impl(context, expected_value):
    valor_variavel = context.variable_result
    assert_equal(
        context, valor_variavel, expected_value,
        "O resultado esperado [%s] e diferente do retorno [%s]." % (expected_value, valor_variavel)
    )
