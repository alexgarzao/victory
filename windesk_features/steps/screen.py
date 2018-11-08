from behave import given, then, when


@given(u'que estou na tela {screen}')  # noqa: F811
def step_impl(context, screen):
    context.module.driver.screen_assert_equal(screen)


@given(u'que vou para a tela {screen}')  # noqa: F811
@given(u'vou para a tela {screen}')
@when(u'vou para a tela {screen}')
@then(u'vou para a tela {screen}')
def step_impl(context, screen):
    context.module.driver.open_screen(screen)


@then('sou direcionado para a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    context.module.driver.screen_assert_equal(screen)


@then('sou direcionado para uma nova janela com a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    # REFACTOR: STEPs nao deveriam ter logica
    context.module.driver.follow_new_window()
    context.module.driver.screen_assert_equal(screen)


@then('sou direcionado para a janela anterior com a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    # REFACTOR: STEPs nao deveriam ter logica
    context.module.driver.return_previous_window()
    context.module.driver.screen_assert_equal(screen)


@then('sou direcionado para o frame anterior')  # noqa: F811
def step_impl(context):
    context.module.driver.switch_to_default()


@then('volto para a janela anterior com a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    # REFACTOR: STEPs nao deveriam ter logica
    context.module.driver.return_previous_window()
    context.module.driver.screen_assert_equal(screen)


@then('sou direcionado para o frame {frame}')  # noqa: F811
def step_impl(context, frame):
    context.module.driver.switch_to_frame(frame)
