from behave import given, then


@given(u'a configuração {config_name} é {config_value}')  # noqa: F811
def step_impl(context, config_name, config_value):
    context.config.set(config_name, config_value)


@given(u'que a configuração está na tabela abaixo')  # noqa: F811
def step_impl(context):
    for row in context.table:
        context.config.set(name=row['nome'], value=row['valor'])
    context.config_scenario = True


@then(u'o teste é iniciado')  # noqa: F811
def step_impl(context):
    # REFACTOR: STEPs nao deveriam ter logica
    features_path = context.features_path
    path = features_path + "/" + context.config.get_string('FILES_PATH')
    headless = context.userdata.getbool("headless", context.config.get_bool('HEADLESS'))
    context.config.driver.open(headless, path)
    if headless:
        context.config.set('SLEEP_BETWEEN_STEPS', 0)
