class Definition:
    def __init__(self):
        self.uses_number = 0

    def inc_uses_number(self):
        self.uses_number += 1

    def get_uses_number(self):
        return self.uses_number
