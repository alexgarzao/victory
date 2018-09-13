from behave import given, then


@given(u'que estou na tela {screen}')  # noqa: F811
def step_impl(context, screen):
    context.driver.screen_assert_equal(screen)


@given(u'que vou para a tela {screen}')  # noqa: F811
@given(u'vou para a tela {screen}')
def step_impl(context, screen):
    context.driver.open_screen(screen)


# @given(u'preencho o campo de nome {campo} com o valor {valor} valor esperado {valor_esperado}')
# def step_impl(context, campo, valor, valor_esperado):
#     if not valor == "<ignora>":
#         context.driver.find_element_by_name(campo).send_keys(valor)
#         set_value = context.driver.find_element_by_name(campo).get_attribute('value')
#         assert set_value == valor_esperado
#     else:
#         pass


@then('sou direcionado para a url que inicia em {url}')  # noqa: F811
def step_impl(context, url):
    context.driver.url_assert_start_with(url)


@given('estou na url {url}')  # noqa: F811
@then('sou direcionado para a url {url}')
def step_impl(context, url):
    context.driver.url_assert_equal(url)


@then('sou direcionado para a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    context.driver.screen_assert_equal(screen)


@then('sou direcionado para uma nova janela com a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    # REFACTOR: STEPs nao deveriam ter logica
    context.driver.follow_new_window()
    context.driver.screen_assert_equal(screen)


@then('sou direcionado para a janela anterior com a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    # REFACTOR: STEPs nao deveriam ter logica
    context.driver.return_previous_window()
    context.driver.screen_assert_equal(screen)


@then('sou direcionado para o frame anterior')  # noqa: F811
def step_impl(context):
    context.driver.switch_to_default()


@then('volto para a janela anterior com a tela {screen}')  # noqa: F811
def step_impl(context, screen):
    # REFACTOR: STEPs nao deveriam ter logica
    context.driver.return_previous_window()
    context.driver.screen_assert_equal(screen)


@then('sou direcionado para o frame {frame}')  # noqa: F811
def step_impl(context, frame):
    context.driver.switch_to_frame(frame)
