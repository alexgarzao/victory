class Events:
    def __init__(self):
        self.events = {}

    def add(self, event_name, event_step):
        if event_name not in self.events:
            self.events[event_name] = []

        event = self.events[event_name]
        event.append(event_step)

    def run(self, context, event_name):
        assert event_name in self.events
        if event_name not in self.events:
            assert False
            context.execute_steps("quando " + event_name)
            return

        event = self.events[event_name]
        for step_event in event:
            context.execute_steps("quando " + step_event)
