from .events import EventList


class ApiDriver:
    def __init__(self):
        self.event_list = EventList()
        self.base_url = None

    def add_event(self, event_name):
        return self.event_list.add(self.base_url, event_name)

    def get_event(self, event_name):
        return self.event_list.get(event_name)

    def set_base_url(self, url):
        self.base_url = url
