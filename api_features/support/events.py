from .request import Request


class Event(object):
    def __init__(self, resource):
        self.resource = resource
        self.path = None
        self.method = None

    def set_path(self, value):
        self.path = value

    def set_method(self, value):
        self.method = value

    def get_new_request(self):
        return Request(self)


class EventList(object):
    def __init__(self):
        self.__event_list = {}

    def add(self, alias, resource):
        event = Event(resource)
        self.__event_list[alias] = event
        return event

    def get(self, alias):
        return self.__event_list[alias]

    def find(self, alias):
        return self.__event_list.get(alias, None)
