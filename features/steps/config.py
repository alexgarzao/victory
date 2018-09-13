from behave import given, then


@given(u'a configuração {config_name} é {config_value}')  # noqa: F811
def step_impl(context, config_name, config_value):
    context.test_config.set(config_name, config_value)


@given(u'que a configuração está na tabela abaixo')  # noqa: F811
def step_impl(context):
    for row in context.table:
        context.test_config.set(name=row['nome'], value=row['valor'])
    context.config_scenario = True


@then(u'o teste é iniciado')  # noqa: F811
def step_impl(context):
    # REFACTOR: STEPs nao deveriam ter logica
    context.test_config.load_from_command_line(context.config.userdata)
    features_path = context.test_config.get_string("FEATURES_PATH")
    path = features_path + "/" + context.test_config.get_string('FILES_PATH')
    headless = context.test_config.get_bool('HEADLESS')

    if headless:
        context.test_config.set('SLEEP_BETWEEN_STEPS', 0)

    context.driver.open(headless, path)
