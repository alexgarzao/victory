import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from common import value_with_mask


@given(u'que quero definir os elementos da tela')
def step_impl(context):
    pass


@then(u'o elemento {name} tem o id {internal_id}')
def step_impl(context, name, internal_id):
    context.config.driver.new_id_element(name, internal_id)


@then(u'o elemento {name} tem o nome {internal_name}')
def step_impl(context, name, internal_name):
    context.config.driver.new_name_element(name, internal_name)


@then(u'o elemento {name} tem o texto {internal_text}')
def step_impl(context, name, internal_text):
    context.config.driver.new_text_element(name, internal_text)


@then(u'o elemento {name} tem o xpath {internal_xpath}')
def step_impl(context, name, internal_xpath):
    context.config.driver.new_xpath_element(name, internal_xpath)


@then(u'o elemento {name} tem o automation id {internal_automation_id}')
def step_impl(context, name, internal_automation_id):
    context.config.driver.new_automation_id_element(name, internal_automation_id)


@then(u'o elemento {name} tem a classe {class_name}')
def step_impl(context, name, class_name):
    context.config.driver.new_class_name_element(name, class_name)


@step(u'vejo o {name} com o valor {expected_value}')
def step_impl(context, name, expected_value):
    element = context.config.driver.find_element(name)
    value = context.config.driver.search_text(element)
    assert value == expected_value


@step(u'preencho o {name} com o valor {value}')
@step(u'preencho a {name} com o valor {value}')
def step_impl(context, name, value):
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    context.config.driver.find_element(name).clear()
    context.config.driver.find_element(name).send_keys(value + Keys.TAB)


@step(u'seleciono o {name} e digito {value}')
@step(u'seleciono a {name} e digito {value}')
def step_impl(context, name, value):
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    element_to_hover_over = context.config.driver.find_element(name)
    hover = ActionChains(context.config.driver.driver).move_to_element(element_to_hover_over).click().send_keys(value + Keys.ENTER)
    hover.perform()


@step(u'seleciono o {name} e pressiono a seta para baixo {value:d} vezes')
@step(u'seleciono a {name} e pressiono a seta para baixo {value:d} vezes')
@step(u'seleciono o {name} e pressiono a seta para baixo {value:d} vez')
@step(u'seleciono a {name} e pressiono a seta para baixo {value:d} vez')
def step_impl(context, name, value):
    element_to_hover_over = context.config.driver.find_element(name)

    keys = ''
    for k in range(value):
        keys += Keys.DOWN

    keys += Keys.ENTER

    hover = ActionChains(context.config.driver.driver).move_to_element(element_to_hover_over).click().send_keys(keys).perform()


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


@step(u'clico no {name}')
@step(u'clico em {name}')
def step_impl(context, name):
    #TODO: Ver se o elemento pode estar visivel mas nao clicavel
    #TODO: Precisa validar se esta habilitado?!
    for i in range(0, 10):
        try:
            context.config.driver.find_element(name).click()
            return
        except:
            time.sleep(1)
    assert False, "Elemento %s nao encontrado ou nao pode receber o evento click" % name


@when(u'flutuo no {name}')
def step_impl(context, name):
    for i in range(0, 10):
        try:
            element_to_hover_over = context.config.driver.find_element(name)
            hover = ActionChains(context.config.driver.driver).move_to_element(element_to_hover_over)
            hover.perform()
            return
        except:
            time.sleep(1)
    assert False, "Elemento %s nao encontrado ou nao pode receber o evento hover" % name


@step(u'aguardo {seconds:Number} segundo')
@step(u'aguardo {seconds:Number} segundos')
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


@then(u'a tela {name} é {url}')
def step_impl(context, name, url):
    context.config.driver.new_screen(name, url)


@then(u'eu aceito a popup')
def step_impl(context):
    # Switch to alert.
    popup = context.config.driver.driver.switch_to.alert

    # Use the accept() method to accept the alert
    popup.accept()


@then(u'fica visível a {element_name}')
def step_impl(context, element_name):
    for i in range(0, 10):
        try:
            assert context.config.driver.find_element(element_name).is_displayed == False
            return
        except:
            time.sleep(1)
    assert False, 'Elemento %s nao esta visivel' % element_name
