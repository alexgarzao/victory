from selenium.webdriver.support.ui import WebDriverWait


from .element import IdElement, TextElement, NameElement, XpathElement, AutomationIdElement, ClassNameElement, \
    CssSelectorElement
from features.support.actions import Actions
from features.support.definition import Definition


class Screen(Definition):
    def __init__(self, driver, name):
        super().__init__()
        self.driver = driver
        self.name = name
        self.url = ""
        self.elements = {}
        self.actions = Actions()

    def add_id_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, IdElement(self.driver, self.name, name, internal_id, ignore_displayed))

    def add_text_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, TextElement(self.driver, self.name, name, internal_id, ignore_displayed))

    def add_name_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, NameElement(self.driver, self.name, name, internal_id, ignore_displayed))

    def add_xpath_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, XpathElement(self.driver, self.name, name, internal_id, ignore_displayed))

    def add_automation_id_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, AutomationIdElement(self.driver, self.name, name, internal_id, ignore_displayed))

    def add_class_name_element(self, name, class_name, ignore_displayed=False):
        self.__add_element(name, ClassNameElement(self.driver, self.name, name, class_name, ignore_displayed))

    def add_css_selector_element(self, name, css, ignore_displayed=False):
        self.__add_element(name, CssSelectorElement(self.driver, self.name, name, css, ignore_displayed))

    def add_action(self, name):
        self.actions.add_action(name)

    def add_event_in_action(self, action_name, event):
        self.actions.add_event(action_name, event)

    def get_steps_to_execute(self, action_name):
        return self.actions.get_steps_to_execute(action_name)

    def find_element(self, name, parameter=None):
        name = name.lower()
        element = self.elements.get(name)
        if element is None:
            possible = ','.join(list(self.elements))
            raise ElementNotFoundException("Element {} not found. Possible values: {}".format(name, possible))

        element.inc_uses_number()
        self.__wait_for_ajax()
        return element.find_element(parameter)

    def get_element(self, name):
        name = name.lower()
        return self.elements.get(name)

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_name(self):
        return self.name

    def get_unused_elements(self):
        unused_elements = [element for key, element in self.elements.items() if element.get_uses_number() == 0]
        return unused_elements

    def __add_element(self, name, new_element):
        name = name.lower()
        if self.elements.get(name) is not None:
            raise DuplicatedElementException("Element {} already exists".format(name))

        self.elements[name] = new_element

    def __wait_for_ajax(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
            wait.until(lambda driver: self.driver.execute_script('return document.readyState == "complete"'))
        except Exception as e:
            pass


class DuplicatedElementException(Exception):
    pass


class ElementNotFoundException(Exception):
    pass
