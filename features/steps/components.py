import time
import os

from behave import given, then, step, when
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from common import value_with_mask


@given(u'que quero definir os elementos da tela {screen_name}')  # noqa: F811
def step_impl(context, screen_name):
    context.config.driver.new_screen(screen_name)
    context.config_scenario = True


@then(u'os elementos são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        element = row['elemento']
        method = row['método']
        id = row['identificação']
        context.execute_steps(u'Então o elemento {} tem o {} {}'.format(element, method, id))


@then(u'o elemento {name} tem o id {internal_id} ignorando is_displayed')  # noqa: F811
def step_impl(context, name, internal_id):
    context.config.driver.current_screen.add_id_element(name, internal_id, ignore_displayed=True)


@then(u'o elemento {name} tem o id {internal_id}')  # noqa: F811
def step_impl(context, name, internal_id):
    context.config.driver.current_screen.add_id_element(name, internal_id, ignore_displayed=False)


@then(u'o elemento {name} tem o nome {internal_name} ignorando is_displayed')  # noqa: F811
def step_impl(context, name, internal_name):
    context.config.driver.current_screen.add_name_element(name, internal_name, ignore_displayed=True)


@then(u'o elemento {name} tem o nome {internal_name}')  # noqa: F811
def step_impl(context, name, internal_name):
    context.config.driver.current_screen.add_name_element(name, internal_name, ignore_displayed=False)


@then(u'o elemento {name} tem o texto {internal_text} ignorando is_displayed')  # noqa: F811
def step_impl(context, name, internal_text):
    context.config.driver.current_screen.add_text_element(name, internal_text, ignore_displayed=True)


@then(u'o elemento {name} tem o texto {internal_text}')  # noqa: F811
def step_impl(context, name, internal_text):
    context.config.driver.current_screen.add_text_element(name, internal_text, ignore_displayed=False)


@then(u'o elemento {name} tem o xpath {internal_xpath} ignorando is_displayed')  # noqa: F811
def step_impl(context, name, internal_xpath):
    context.config.driver.current_screen.add_xpath_element(name, internal_xpath, ignore_displayed=True)


@then(u'o elemento {name} tem o xpath {internal_xpath}')  # noqa: F811
def step_impl(context, name, internal_xpath):
    context.config.driver.current_screen.add_xpath_element(name, internal_xpath, ignore_displayed=False)


@then(u'o elemento {name} tem o automation id {internal_automation_id} ignorando is_displayed')  # noqa: F811
def step_impl(context, name, internal_automation_id):
    context.config.driver.current_screen.add_automation_id_element(name, internal_automation_id, ignore_displayed=True)


@then(u'o elemento {name} tem o automation id {internal_automation_id}')  # noqa: F811
def step_impl(context, name, internal_automation_id):
    context.config.driver.current_screen.add_automation_id_element(name, internal_automation_id, ignore_displayed=False)


@then(u'o elemento {name} tem a classe {class_name} ignorando is_displayed')  # noqa: F811
@then(u'o elemento {name} tem o classe {class_name} ignorando is_displayed')
def step_impl(context, name, class_name):
    context.config.driver.current_screen.add_class_name_element(name, class_name, ignore_displayed=True)


@then(u'o elemento {name} tem a classe {class_name}')  # noqa: F811
@then(u'o elemento {name} tem o classe {class_name}')
def step_impl(context, name, class_name):
    context.config.driver.current_screen.add_class_name_element(name, class_name, ignore_displayed=False)


@step(u'vejo o {name} com o valor {expected_value}')  # noqa: F811
def step_impl(context, name, expected_value):
    # REFACTOR: STEPs nao deveriam ter logica
    element = context.config.driver.current_screen.find_element(name)
    value = context.config.driver.current_screen.search_text(element)
    assert value == expected_value


@step(u'preencho o {component_name} com a consulta {query_name}')  # noqa: F811
@step(u'preencho a {component_name} com a consulta {query_name}')
def step_impl(context, component_name, query_name):
    # REFACTOR: STEPs nao deveriam ter logica
    value = context.config.driver.queries.run(query_name)
    element = context.config.driver.current_screen.find_element(component_name)
    element.clear()
    element.send_keys(value + Keys.TAB)


@step(u'preencho o {name} com o valor {value}')  # noqa: F811
@step(u'preencho a {name} com o valor {value}')
def step_impl(context, name, value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    element = context.config.driver.current_screen.find_element(name)
    element.clear()
    element.send_keys(value + Keys.TAB)


@step(u'faço o upload do arquivo {fileid} no {element_name}')  # noqa: F811
def step_impl(context, fileid, element_name):
    # REFACTOR: STEPs nao deveriam ter logica
    element = context.config.driver.current_screen.find_element(element_name)
    filename = context.config.driver.get_filename(fileid)
    full_path = os.path.abspath(filename)
    element.send_keys(full_path)


@step(u'seleciono o {name} e digito {value}')  # noqa: F811
@step(u'seleciono a {name} e digito {value}')
def step_impl(context, name, value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    element_to_hover_over = context.config.driver.current_screen.find_element(name)
    hover = ActionChains(context.config.driver.driver).\
        move_to_element(element_to_hover_over).\
        click().\
        send_keys(value + Keys.ENTER)
    hover.perform()


@step(u'seleciono o {name} e pressiono a seta para baixo {value:d} vezes')  # noqa: F811
@step(u'seleciono a {name} e pressiono a seta para baixo {value:d} vezes')
@step(u'seleciono o {name} e pressiono a seta para baixo {value:d} vez')
@step(u'seleciono a {name} e pressiono a seta para baixo {value:d} vez')
def step_impl(context, name, value):
    # REFACTOR: STEPs nao deveriam ter logica
    element_to_hover_over = context.config.driver.current_screen.find_element(name)

    keys = ''
    for k in range(value):
        keys += Keys.DOWN

    keys += Keys.ENTER

    hover = ActionChains(context.config.driver.driver).\
        move_to_element(element_to_hover_over).\
        click().\
        send_keys(keys)
    hover.perform()


@given(u'preencho e valido o {name} com o valor {value} e valor esperado {expected_value}')  # noqa: F811
def step_impl(context, name, value, expected_value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    element = context.config.driver.current_screen.find_element(name)
    element.clear()
    element.send_keys(value)
    set_value = element.get_attribute('value')
    assert set_value == expected_value


@given(u'preencho e valido o {name} com o valor {value} e máscara {mask}')  # noqa: F811
def step_impl(context, name, value, mask):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return

    element = context.config.driver.current_screen.find_element(name)
    element.clear()
    element.send_keys(value)
    set_value = element.get_attribute('value')
    expected_value = value_with_mask(value, mask)
    assert set_value == expected_value


@step(u'clico no {name}')  # noqa: F811
@step(u'clico na {name}')
@step(u'clico em {name}')
def step_impl(context, name):
    # TODO: Precisa validar se esta habilitado?! visivel? clicavel?
    # TODO: remover logica do step :-)
    context.config.driver.current_screen.find_element(name).click()


@when(u'flutuo no {name}')  # noqa: F811
def step_impl(context, name):
    # REFACTOR: STEPs nao deveriam ter logica
    # TODO: remover logica do step :-)
    # TODO: Mas, para remover a logica, talvez eu tenha que abstrair os elementos
    # TODO: Hoje, find_element retorna o elemento do webdriver diretamente...
    element_to_hover_over = context.config.driver.current_screen.find_element(name)
    hover = ActionChains(context.config.driver.driver).move_to_element(element_to_hover_over)
    hover.perform()


@step(u'aguardo {seconds:Number} segundo')  # noqa: F811
@step(u'aguardo {seconds:Number} segundos')
def step_impl(context, seconds):
    time.sleep(seconds)


@given(u'seleciono em {name} o valor {value}')  # noqa: F811
def step_impl(context, name, value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    select = Select(context.config.driver.current_screen.find_element(name))
    select.select_by_visible_text(value)
    selected_option = select.first_selected_option
    set_value = selected_option.text
    assert set_value == value


@then(u'seleciono nas {name} a opção {option}')  # noqa: F811
def step_impl(context, name, option):
    element = context.config.driver.current_screen.find_element(name, option)
    element.click()


@step(u'a URL é {url}')  # noqa: F811
def step_impl(context, url):
    context.config.driver.current_screen.set_url(url)


@then(u'eu aceito a popup')  # noqa: F811
def step_impl(context):
    # REFACTOR: STEPs nao deveriam ter logica
    # Switch to alert.
    popup = context.config.driver.driver.switch_to.alert

    # Use the accept() method to accept the alert
    popup.accept()


@then(u'fica visível a {element_name}')  # noqa: F811
def step_impl(context, element_name):
    # TODO: remover logica do step :-)
    assert context.config.driver.current_screen.find_element(element_name).is_displayed() is True
