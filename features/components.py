# TODO: Trocar de Component para Element...

class Component(object):
    def __init__(self, driver, name, internal_id):
        self.driver = driver
        self.name = name
        self.internal_id = internal_id

    # def get_internal_id(self):
    #     return self.internal_id
    #
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


class IdComponent(Component):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_xpath('//*[@id="' + self.internal_id + '"]')


class TextComponent(Component):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_xpath('//*[text()='+ self.internal_id +']')


class NameComponent(Component):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_name(self.internal_id)


class XpathComponent(Component):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_xpath(self.internal_id)


class AutomationIdComponent(Component):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_xpath('//*[@data-automation-id="' + self.internal_id + '"]')



class Components(object):
    def __init__(self, driver):
        self.driver = driver
        self.clear()

    def clear(self):
        self.list = {}

    def new_id_component(self, name, internal_id):
        self.list[name] = IdComponent(self.driver, name, internal_id)

    def new_text_component(self, name, internal_id):
        self.list[name] = TextComponent(self.driver, name, internal_id)

    def new_name_component(self, name, internal_id):
        self.list[name] = NameComponent(self.driver, name, internal_id)

    def new_xpath_component(self, name, internal_id):
        self.list[name] = XpathComponent(self.driver, name, internal_id)

    def new_automation_id_component(self, name, internal_id):
        self.list[name] = AutomationIdComponent(self.driver, name, internal_id)

    def get_element(self, name):
        return self.list[name].find_element()

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
