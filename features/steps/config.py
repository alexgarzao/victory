from behave import given, then


@given(u'que a configuração está na tabela abaixo')  # noqa: F811
def step_impl(context):
    for row in context.table:
        context.test_config.set(name=row['nome'], value=row['valor'])
    context.config_scenario = True


@then(u'o teste é iniciado')  # noqa: F811
def step_impl(context):
    # REFACTOR: STEPs nao deveriam ter logica
    context.test_config.load_from_command_line(context.config.userdata)
    context.module.start()
