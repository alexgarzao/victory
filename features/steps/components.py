import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from common import value_with_mask


@given(u'que quero definir os elementos da tela')
def step_impl(context):
    context.config.driver.clear_elements()


@given(u'que o elemento {name} tem o id {internal_id}')
def step_impl(context, name, internal_id):
    context.config.driver.new_id_element(name, internal_id)


@given(u'que o elemento {name} tem o nome {internal_name}')
def step_impl(context, name, internal_name):
    context.config.driver.new_name_element(name, internal_name)


@given(u'que o elemento {name} tem o texto {internal_text}')
def step_impl(context, name, internal_text):
    context.config.driver.new_text_element(name, internal_text)


@given(u'que o elemento {name} tem o xpath {internal_xpath}')
def step_impl(context, name, internal_xpath):
    context.config.driver.new_xpath_element(name, internal_xpath)


@given(u'que o elemento {name} tem o automation id {internal_automation_id}')
def step_impl(context, name, internal_automation_id):
    context.config.driver.new_automation_id_element(name, internal_automation_id)


@when(u'tento definir os elementos')
def step_impl(context):
    pass


@then(u'recebo um ok')
def step_impl(context):
    pass


@given(u'vejo o {name} com o valor {expected_value}')
@then(u'vejo o {name} com o valor {expected_value}')
def step_impl(context, name, expected_value):
    element = context.config.driver.find_element(name)
    value = context.config.driver.search_text(element)
    assert value == expected_value


@given(u'preencho o {name} com o valor {value}')
@given(u'preencho a {name} com o valor {value}')
def step_impl(context, name, value):
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    context.config.driver.find_element(name).clear()
    context.config.driver.find_element(name).send_keys(value + Keys.TAB)


@given(u'preencho e valido o {name} com o valor {value} e valor esperado {expected_value}')
def step_impl(context, name, value, expected_value):
    if value == "<ignora>":
        return
    context.config.driver.find_element(name).clear()
    context.config.driver.find_element(name).send_keys(value)
    set_value = context.config.driver.find_element(name).get_attribute('value')
    assert set_value == expected_value


@given(u'preencho e valido o {name} com o valor {value} e máscara {mask}')
def step_impl(context, name, value, mask):
    if value == "<ignora>":
        return

    context.config.driver.find_element(name).clear()
    context.config.driver.find_element(name).send_keys(value)
    set_value = context.config.driver.find_element(name).get_attribute('value')
    expected_value = value_with_mask(value, mask)
    assert set_value == expected_value


@then(u'clico no {name}')
@given(u'clico no {name}')
@when(u'clico no {name}')
def step_impl(context, name):
    #TODO: Ver se o elemento pode estar visivel mas nao clicavel
    #TODO: Precisa validar se esta habilitado?!
    for i in range(0, 10):
        try:
            context.config.driver.find_element(name).click()
            return
        except:
            time.sleep(1)


@when(u'aguardo {seconds:Number} segundo')
@given(u'aguardo {seconds:Number} segundo')
@when(u'aguardo {seconds:Number} segundos')
@given(u'aguardo {seconds:Number} segundos')
def step_impl(context, seconds):
    time.sleep(seconds)


@given(u'seleciono em {name} o valor {value}')
def step_impl(context, name, value):
    if value == "<ignora>":
        return
    select = Select(context.config.driver.find_element(name))
    select.select_by_visible_text(value)
    selected_option = select.first_selected_option
    set_value = selected_option.text
    assert set_value == value


@given(u'que a tela {name} é {url}')
def step_impl(context, name, url):
    context.config.driver.new_screen(name, url)
