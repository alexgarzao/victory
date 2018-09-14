from api_features.actions import ActionList


class ApiDriver:
    def __init__(self):
        self.action_list = ActionList()
        self.base_url = None

    def add_action(self, action_name):
        return self.action_list.add(self.base_url, action_name)

    def get_action(self, action_name):
        return self.action_list.get(action_name)

    def set_base_url(self, url):
        self.base_url = url
