from parse import *


class Actions:
    def __init__(self):
        self.actions = {}

    def add(self, action_name, event):
        if action_name not in self.actions:
            self.actions[action_name] = []

        events = self.actions[action_name]
        events.append(event)

    def run(self, context, action_name):
        # TODO: retornar steps aos inves de executar. Assim nao precisa conhecer context.
        events, parameters = self.__match_action(action_name)
        assert events != None
        steps_to_run = ''
        for event in events:
            step_event = self.__replace_parameters(event, parameters)
            steps_to_run += step_event + '\n'

        context.execute_steps(steps_to_run)

    def __match_action(self, action):
        for action_type in self.actions.keys():
            r = parse(action_type, action)
            if r:
                return self.actions[action_type], r.named

        return None

    def __replace_parameters(self, step, parameters):
        for parameter, value in parameters.items():
            token_to_find = "{" + parameter + "}"
            step = step.replace(token_to_find, value)

        return step
