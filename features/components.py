# TODO: REFACTOR: Cada componente deveria ser uma classe distinta...
# TODO: Trocar de Component para Element...

class Component(object):
    ID = 1
    TEXT = 2
    NAME = 3
    XPATH = 4
    AUTOMATION_ID = 5

    def __init__(self, name, type, internal_id):
        self.name = name
        self.type = type
        self.internal_id = internal_id

    def get_internal_id(self):
        return self.internal_id


class Components(object):
    def __init__(self, driver):
        self.driver = driver
        self.clear()

    def clear(self):
        self.list = {}

    def new_id_component(self, name, internal_id):
        self.list[name] = Component(name, Component.ID, internal_id)

    def new_text_component(self, name, internal_id):
        self.list[name] = Component(name, Component.TEXT, internal_id)

    def new_name_component(self, name, internal_id):
        self.list[name] = Component(name, Component.NAME, internal_id)

    def new_xpath_component(self, name, internal_id):
        self.list[name] = Component(name, Component.XPATH, internal_id)

    def new_automation_id_component(self, name, internal_id):
        self.list[name] = Component(name, Component.AUTOMATION_ID, internal_id)

    def get_element(self, name):
        component = self.list[name]

        if component.type == component.ID:
            element = self.find_element_by_xpath('//*[@id="' + component.internal_id + '"]')
        elif component.type == component.TEXT:
            element = self.find_element_by_xpath('//*[text()='+ component.internal_id +']')
        elif component.type == component.NAME:
            element = self.find_element_by_name(component.internal_id)
        elif component.type == component.XPATH:
            element = self.find_element_by_xpath(component.internal_id)
        elif component.type == component.AUTOMATION_ID:
            element = self.find_element_by_xpath('//*[@data-automation-id="' + component.internal_id + '"]')
        else:
            assert False, 'Invalid component type'

        assert element != None, 'Componente "%s" nao encontrado' % component.internal_id
        return element

    def find_element_by_xpath(self, xpath):
        return self.__try_to_get_element(self.driver.find_element_by_xpath, xpath)

    def find_element_by_id(self, id):
        return self.__try_to_get_element(self.driver.find_element_by_id, id)

    def find_element_by_name(self, name):
        return self.__try_to_get_element(self.driver.find_element_by_name, name)

    def find_element_by_automation_id(self, id):
        return self.__try_to_get_element(self.driver.find_element_by_xpath, id)

    def __try_to_get_element(self, func, parameter):
        for retries in range(0, 5):
            el = func(parameter)
            if el and el.is_displayed: # and el.is_enabled:
                return el
            time.sleep(1)
        return None
