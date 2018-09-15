class Module:
    def __init__(self, type, context):
        self.type = type
        self.context = context

    def before_all(self):
        pass

    def after_scenario(self, scenario):
        pass

    def after_step(self, step):
        pass

    def after_all(self):
        pass
