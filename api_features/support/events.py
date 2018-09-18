from .request import GetRequest, PutRequest, PostRequest, DeleteRequest


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
        if self.method == 'POST':
            return PostRequest(self)
        elif self.method == 'GET':
            return GetRequest(self)
        elif self.method == 'PUT':
            return PutRequest(self)
        elif self.method == 'DELETE':
            return DeleteRequest(self)
        else:
            assert False


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
