from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

from web_app import WebApp


@given(u'a configuração {config_name} é {config_value}')
def step_impl(context, config_name, config_value):
    context.config.set(config_name, config_value)


@given(u'que a configuração está na tabela abaixo')
def step_impl(context):
    for row in context.table:
        context.config.set(name=row['nome'], value=row['valor'])


@given(u'que estou na tela {screen}')
def step_impl(context, screen):
    context.config.driver.screen_assert_equal(screen)


@given(u'que vou para a tela {screen}')
@given(u'vou para a tela {screen}')
def step_impl(context, screen):
    context.config.driver.open_screen(screen)


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


@then(u'o teste é iniciado')
def step_impl(context):
    context.config.driver.open(context.config.get_bool('HEADLESS'))


@then('sou direcionado para a tela {screen}')
def step(context, screen):
    context.config.driver.screen_assert_equal(screen)
