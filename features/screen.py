from selenium.webdriver.support.ui import WebDriverWait


from element import IdElement, TextElement, NameElement, XpathElement, AutomationIdElement, ClassNameElement
from actions import Actions


class Screen:
    def __init__(self, driver):
        self.driver = driver
        self.url = ""
        self.elements = {}
        self.actions = Actions()

    def add_id_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, IdElement(self.driver, name, internal_id, ignore_displayed))

    def add_text_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, TextElement(self.driver, name, internal_id, ignore_displayed))

    def add_name_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, NameElement(self.driver, name, internal_id, ignore_displayed))

    def add_xpath_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, XpathElement(self.driver, name, internal_id, ignore_displayed))

    def add_automation_id_element(self, name, internal_id, ignore_displayed=False):
        self.__add_element(name, AutomationIdElement(self.driver, name, internal_id, ignore_displayed))

    def add_class_name_element(self, name, class_name, ignore_displayed=False):
        self.__add_element(name, ClassNameElement(self.driver, name, class_name, ignore_displayed))

    def find_element(self, name):
        element = self.elements.get(name)
        if element is None:
            possible = ','.join(list(self.elements))
            raise ElementNotFoundException("Element {} not found. Possible values: {}".format(name, possible))

        self.__wait_for_ajax()
        return element.find_element()

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def __add_element(self, name, new_element):
        if self.elements.get(name) != None:
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
