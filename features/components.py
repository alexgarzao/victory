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
    def __init__(self):
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

    def get_component(self, name):
        return self.list[name]
