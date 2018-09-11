import time


class BaseElement(object):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        self.driver = driver
        self.name = name
        self.internal_id = internal_id
        self.ignore_displayed = ignore_displayed

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

    def find_element_by_css_selector(self, name):
        return self.__try_to_get_element(self.driver.find_element_by_css_selector, name)

    def __try_to_get_element(self, func, parameter):
        for retries in range(0, 5):
            el = func(parameter)
#            if el and el.tag_name == 'select':
#                return el
            if el and el.is_enabled() and (
                    self.ignore_displayed is True or (self.ignore_displayed is False and el.is_displayed())):
                return el
            time.sleep(1)
        return None


class IdElement(BaseElement):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        super().__init__(driver, name, internal_id, ignore_displayed)

    def find_element(self, parameter):
        return self.find_element_by_id(self.internal_id.format(parameter))


class TextElement(BaseElement):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        super().__init__(driver, name, internal_id, ignore_displayed)

    def find_element(self, parameter):
        return self.find_element_by_xpath('//*[text()=' + self.internal_id.format(parameter) + ']')


class NameElement(BaseElement):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        super().__init__(driver, name, internal_id, ignore_displayed)

    def find_element(self, parameter):
        return self.find_element_by_name(self.internal_id.format(parameter))


class XpathElement(BaseElement):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        super().__init__(driver, name, internal_id, ignore_displayed)

    def find_element(self, parameter):
        return self.find_element_by_xpath(self.internal_id.format(parameter))


class AutomationIdElement(BaseElement):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        super().__init__(driver, name, internal_id, ignore_displayed)

    def find_element(self, parameter):
        return self.find_element_by_xpath('//*[@data-automation-id="' + self.internal_id.format(parameter) + '"]')


class ClassNameElement(BaseElement):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        super().__init__(driver, name, internal_id, ignore_displayed)

    def find_element(self, parameter):
        return self.find_element_by_class_name(self.internal_id.format(parameter))


class CssSelectorElement(BaseElement):
    def __init__(self, driver, name, internal_id, ignore_displayed):
        super().__init__(driver, name, internal_id, ignore_displayed)

    def find_element(self, parameter):
        return self.find_element_by_css_selector(self.internal_id.format(parameter))
