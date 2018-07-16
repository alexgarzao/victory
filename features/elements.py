from element import IdElement, TextElement, NameElement, XpathElement, AutomationIdElement


class Elements(object):
    def __init__(self, driver):
        self.driver = driver
        self.clear()

    def clear(self):
        self.list = {}

    def new_id_element(self, name, internal_id):
        self.list[name] = IdElement(self.driver, name, internal_id)

    def new_text_element(self, name, internal_id):
        self.list[name] = TextElement(self.driver, name, internal_id)

    def new_name_element(self, name, internal_id):
        self.list[name] = NameElement(self.driver, name, internal_id)

    def new_xpath_element(self, name, internal_id):
        self.list[name] = XpathElement(self.driver, name, internal_id)

    def new_automation_id_element(self, name, internal_id):
        self.list[name] = AutomationIdElement(self.driver, name, internal_id)

    def get_element(self, name):
        return self.list[name].find_element()
