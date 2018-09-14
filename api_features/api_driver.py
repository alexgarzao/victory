from api_features.endpoints import EndpointList


class ApiDriver:
    def __init__(self):
        self.__current_endpoint = None
        self.endpoint_list = EndpointList()
        self.base_url = None

    def add_endpoint(self, endpoint_name):
        self.__current_endpoint = self.endpoint_list.add(self.base_url, endpoint_name)

    def get_current_endpoint(self):
        return self.__current_endpoint

    def get_endpoint(self, endpoint_name):
        return self.endpoint_list.get(endpoint_name)

    def set_base_url(self, url):
        self.base_url = url
