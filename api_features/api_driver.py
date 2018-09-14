from api_features.actions import ActionList


class ApiDriver:
    def __init__(self):
        self.__current_action = None
        self.action_list = ActionList()
        self.base_url = None

    def add_action(self, action_name):
        self.__current_action = self.action_list.add(self.base_url, action_name)

    def get_current_action(self):
        return self.__current_action

    def get_action(self, action_name):
        return self.action_list.get(action_name)

    def set_base_url(self, url):
        self.base_url = url
