class SimpleResult:
    def __init__(self, value):
        self.value = value

    def get_value(self, resource, unused):
        return self.value
