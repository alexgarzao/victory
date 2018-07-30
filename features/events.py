from parse import *


class Events:
    def __init__(self):
        self.events = {}

    def add(self, event_name, event_step):
        if event_name not in self.events:
            self.events[event_name] = []

        event = self.events[event_name]
        event.append(event_step)

    def run(self, context, event_name):
        # TODO: retornar steps aos inves de executar. Assim nao precisa conhecer context.
        event, parameters = self.__match_event(event_name)
        assert event != None
        steps_to_run = ''
        for step_event in event:
            step_event = self.__replace_parameters(step_event, parameters)
            steps_to_run += step_event + '\n'

        context.execute_steps(steps_to_run)

    def __match_event(self, event):
        for event_type in self.events.keys():
            r = parse(event_type, event)
            if r:
                return self.events[event_type], r.named

        return None

    def __replace_parameters(self, step_event, parameters):
        for parameter, value in parameters.items():
            token_to_find = "{" + parameter + "}"
            step_event = step_event.replace(token_to_find, value)

        return step_event
