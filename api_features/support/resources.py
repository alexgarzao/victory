from .fields import Fields
from .http_status_codes import HttpStatusCodeAliasList
from .events import EventList


class Resource(object):
    def __init__(self, base_url, alias):
        self.base_url = base_url
        self.alias = alias
        self.field_list = Fields()
        self.http_status_code_alias_list = HttpStatusCodeAliasList()
        self.event_list = EventList()

    def add_field(self, name, type, field, location, initial_value):
        self.field_list.add(name, type, field, location, initial_value)

    def get_field(self, name):
        return self.field_list.get(name)

    def get_field_by_name(self, name):
        return self.field_list.get_by_name(name)

    def add_status_code_alias(self, http_status_code, alias):
        self.http_status_code_alias_list.add(http_status_code, alias)

    def get_status_code(self, alias):
        return self.http_status_code_alias_list.get(alias)

    def add_event(self, alias):
        return self.event_list.add(alias, self)

    def find_event(self, alias):
        return self.event_list.find(alias)

    def get_initial_headers(self):
        fields = self.field_list.get_fields_in("header")
        return {fields[alias].json_name: fields[alias].initial_value for alias in fields if fields[alias].has_initial_value}

    def get_initial_body(self):
        fields = self.field_list.get_fields_in("body")
        return {fields[alias].json_name: fields[alias].initial_value for alias in fields if fields[alias].has_initial_value}

    def get_initial_parameters(self):
        fields = self.field_list.get_fields_in("path")
        return {fields[alias].json_name: fields[alias].initial_value for alias in fields if fields[alias].has_initial_value}


class ResourceList(object):
    def __init__(self):
        self.__resource_list = {}

    def add(self, base_url, alias):
        resource = Resource(base_url, alias)
        self.__resource_list[alias] = resource
        return resource

    def get(self, alias):
        return self.__resource_list[alias]

    def find_event(self, alias):
        for name, resource in self.__resource_list.items():
            event = resource.find_event(alias)
            if event is not None:
                return event
        assert False, "Event {} not found!".format(alias)
