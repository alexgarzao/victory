from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

from web_app import WebApp


@given(u'que quero {something}')
def step_impl(context, something):
    pass


@given(u'o app a ser testado está em {app}')
def step_impl(context, app):
    context.config.server_address = app


@given(u'quero rodar os testes no modo {mode}')
def step_impl(context, mode):
    context.config.headless = True


@given(u'estou na tela {screen}')
def step_impl(context, screen):
    context.config.driver.screen_assert_equal(screen)


@given(u'seleciono a select {name} com o texto {texto}')
def step_impl(context, name, texto):
    if not texto == "<ignora>":
        select = Select(context.config.driver.find_element_by_name(name))
        select.select_by_visible_text(texto)
        selected_option = select.first_selected_option
        set_value = selected_option.text
        assert set_value == texto
    else:
        pass


# @given(u'preencho o campo de nome {campo} com o valor {valor} valor esperado {valor_esperado}')
# def step_impl(context, campo, valor, valor_esperado):
#     if not valor == "<ignora>":
#         context.config.driver.find_element_by_name(campo).send_keys(valor)
#         set_value = context.config.driver.find_element_by_name(campo).get_attribute('value')
#         assert set_value == valor_esperado
#     else:
#         pass


@then('sou direcionado para a url que inicia em {url}')
def step(context, url):
    context.config.driver.url_assert_start_with(url)


@given('estou na url {url}')
@then('sou direcionado para a url {url}')
def step(context, url):
    context.config.driver.url_assert_equal(url)


@when(u'tento inicializar o teste')
def step_impl(context):
    context.config.driver.app = context.config.server_address
    context.config.driver.open(context.config.headless)


@then(u'recebo um status ok')
def step_impl(context):
    pass


@then(u'finalizo o teste')
def step_impl(context):
    pass


@then('sou direcionado para a tela de {screen}')
def step(context, screen):
    context.config.driver.screen_assert_equal(screen)
