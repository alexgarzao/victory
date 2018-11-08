import time

from behave import given, then, step, when
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from features.support.mask import value_with_mask


@given(u'que quero definir os elementos da tela {screen_name}')  # noqa: F811
def step_impl(context, screen_name):
    context.module.driver.add_screen(screen_name)
    context.config_scenario = True


@then(u'os elementos são')  # noqa: F811
def step_impl(context):
    for row in context.table:
        element = row['elemento']
        method = row['método']
        id = row['identificação']
        context.execute_steps(u'Então o elemento {} tem o {} {}'.format(element, method, id))


@then(u'o elemento {name} tem o id {internal_id}')  # noqa: F811
def step_impl(context, name, internal_id):
    context.module.driver.get_current_screen().add_id_element(name, internal_id)


@then(u'o elemento {name} tem o nome {internal_name}')  # noqa: F811
def step_impl(context, name, internal_name):
    context.module.driver.get_current_screen().add_name_element(name, internal_name)


@then(u'o elemento {name} tem o texto {internal_text}')  # noqa: F811
def step_impl(context, name, internal_text):
    context.module.driver.get_current_screen().add_text_element(name, internal_text)


@then(u'o elemento {name} tem o xpath {internal_xpath}')  # noqa: F811
def step_impl(context, name, internal_xpath):
    context.module.driver.get_current_screen().add_xpath_element(name, internal_xpath)


@then(u'o elemento {name} tem o automation id {internal_automation_id}')  # noqa: F811
def step_impl(context, name, internal_automation_id):
    context.module.driver.get_current_screen().add_automation_id_element(
        name, internal_automation_id)


@then(u'o elemento {name} tem a classe {class_name}')  # noqa: F811
@then(u'o elemento {name} tem o classe {class_name}')  # Necessario por causa das tabelas
def step_impl(context, name, class_name):
    context.module.driver.get_current_screen().add_class_name_element(name, class_name)


@then(u'o elemento {name} tem o css {css}')  # noqa: F811
def step_impl(context, name, css):
    context.module.driver.get_current_screen().add_css_selector_element(name, css)


@then(u'vejo o {name} com o valor {expected_value}')  # noqa: F811
@then(u'vejo a {name} com o valor {expected_value}')
def step_impl(context, name, expected_value):
    # REFACTOR: STEPs nao deveriam ter logica
    element = context.module.driver.get_current_screen().find_element(name)
    value = context.module.driver.get_current_screen().search_text(element)
    assert value == expected_value


@given(u'preencho o {component_name} com a consulta {query_name}')  # noqa: F811
@given(u'preencho a {component_name} com a consulta {query_name}')
@when(u'preencho o {component_name} com a consulta {query_name}')
@when(u'preencho a {component_name} com a consulta {query_name}')
def step_impl(context, component_name, query_name):
    # REFACTOR: STEPs nao deveriam ter logica
    value = context.module.queries.run(query_name)
    element = context.module.driver.get_current_screen().find_element(component_name)
    element.clear()
    element.send_keys(value.get_value() + Keys.TAB)


@given(u'preencho o {name} com o valor {value}')  # noqa: F811
@given(u'preencho a {name} com o valor {value}')
@when(u'preencho o {name} com o valor {value}')
@when(u'preencho a {name} com o valor {value}')
@then(u'preencho o {name} com o valor {value}')
@then(u'preencho a {name} com o valor {value}')
def step_impl(context, name, value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    element = context.module.driver.get_current_screen().find_element(name)
    element.clear()
    element.send_keys(value + Keys.TAB)


@step(u'seleciono o {name} e digito {value}')  # noqa: F811
@step(u'seleciono a {name} e digito {value}')
def step_impl(context, name, value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    element_to_hover_over = context.module.driver.get_current_screen().find_element(name)
    hover = ActionChains(context.module.driver.driver).\
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
    element_to_hover_over = context.module.driver.get_current_screen().find_element(name)

    keys = ''
    for k in range(value):
        keys += Keys.DOWN

    keys += Keys.ENTER

    hover = ActionChains(context.module.driver.driver).\
        move_to_element(element_to_hover_over).\
        click().\
        send_keys(keys)
    hover.perform()


@given(u'preencho e valido o {name} com o valor {value} e valor esperado {expected_value}')  # noqa: F811
def step_impl(context, name, value, expected_value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    element = context.module.driver.get_current_screen().find_element(name)
    element.clear()
    element.send_keys(value)
    set_value = element.get_attribute('value')
    assert set_value == expected_value


@given(u'preencho e valido o {name} com o valor {value} e máscara {mask}')  # noqa: F811
def step_impl(context, name, value, mask):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return

    element = context.module.driver.get_current_screen().find_element(name)
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
    context.module.driver.get_current_screen().find_element(name).click()


@when(u'flutuo no {name}')  # noqa: F811
def step_impl(context, name):
    # REFACTOR: STEPs nao deveriam ter logica
    # TODO: remover logica do step :-)
    # TODO: Mas, para remover a logica, talvez eu tenha que abstrair os elementos
    # TODO: Hoje, find_element retorna o elemento do webdriver diretamente...
    element_to_hover_over = context.module.driver.get_current_screen().find_element(name)
    hover = ActionChains(context.module.driver.driver).move_to_element(element_to_hover_over)
    hover.perform()


@step(u'aguardo {seconds:Number} segundo')  # noqa: F811
@step(u'aguardo {seconds:Number} segundos')
@step(u'que aguardo {seconds:Number} segundo')
@step(u'que aguardo {seconds:Number} segundos')
def step_impl(context, seconds):
    time.sleep(seconds)


@given(u'seleciono em {name} o valor {value}')  # noqa: F811
def step_impl(context, name, value):
    # REFACTOR: STEPs nao deveriam ter logica
    if value == "<ignora>":
        return
    select = Select(context.module.driver.get_current_screen().find_element(name))
    select.select_by_visible_text(value)
    selected_option = select.first_selected_option
    set_value = selected_option.text
    assert set_value == value


@then(u'seleciono nas {name} a opção {option}')  # noqa: F811
def step_impl(context, name, option):
    element = context.module.driver.get_current_screen().find_element(name, option)
    element.click()


@then(u'aceito a popup')  # noqa: F811
def step_impl(context):
    # REFACTOR: STEPs nao deveriam ter logica
    # Switch to alert.
    popup = context.module.driver.driver.switch_to.alert

    # Use the accept() method to accept the alert
    popup.accept()


@then(u'fica visível a {element_name}')  # noqa: F811
@then(u'fica visível o {element_name}')
def step_impl(context, element_name):
    # TODO: remover logica do step :-)
    assert context.module.driver.get_current_screen().find_element(element_name).is_displayed() is True


@then(u'verifico que o {element_name} tem o valor {expected_value}')  # noqa: F811
@then(u'verifico que a {element_name} tem o valor {expected_value}')
def step_impl(context, element_name, expected_value):
    element = context.module.driver.get_current_screen().find_element(element_name)
    value = element.get_attribute('value')
    assert value == expected_value
