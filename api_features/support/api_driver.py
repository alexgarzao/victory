from .resources import ResourceList


class ApiDriver:
    def __init__(self):
        self.resource_list = ResourceList()
        self.base_url = None

    def add_resource(self, resource_name):
        return self.resource_list.add(self.base_url, resource_name)

    def get_resource(self, resource_name):
        return self.resource_list.get(resource_name)

    def set_base_url(self, url):
        self.base_url = url

    def find_event(self, alias):
        return self.resource_list.find_event(alias)
