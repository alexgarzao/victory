class BaseElement(object):
    def __init__(self, driver, name, internal_id):
        self.driver = driver
        self.name = name
        self.internal_id = internal_id

    def find_element_by_xpath(self, xpath):
        return self.__try_to_get_element(self.driver.find_element_by_xpath, xpath)

    def find_element_by_id(self, id):
        return self.__try_to_get_element(self.driver.find_element_by_id, id)

    def find_element_by_name(self, name):
        return self.__try_to_get_element(self.driver.find_element_by_name, name)

    def find_element_by_automation_id(self, id):
        return self.__try_to_get_element(self.driver.find_element_by_xpath, id)

    def find_element_by_class_name(self, name):
        return self.__try_to_get_element(self.driver.find_element_by_class_name, name)

    def __try_to_get_element(self, func, parameter):
        for retries in range(0, 5):
            el = func(parameter)
            if el and el.is_displayed() and el.is_enabled():
                return el
            time.sleep(1)
        return None


class IdElement(BaseElement):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_id(self.internal_id)


class TextElement(BaseElement):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_xpath('//*[text()='+ self.internal_id +']')


class NameElement(BaseElement):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_name(self.internal_id)


class XpathElement(BaseElement):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_xpath(self.internal_id)


class AutomationIdElement(BaseElement):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_xpath('//*[@data-automation-id="' + self.internal_id + '"]')


class ClassNameElement(BaseElement):
    def __init__(self, driver, name, internal_id):
        super().__init__(driver, name, internal_id)

    def find_element(self):
        return self.find_element_by_class_name(self.internal_id)
