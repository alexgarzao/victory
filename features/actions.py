from parse import parse


class Actions:
    def __init__(self):
        self.actions = {}

    def new_action(self, action_name):
        action_name = action_name.lower()
        if self.actions.get(action_name) is not None:
            raise DuplicatedActionException("Action {} already exists".format(action_name))

        self.actions[action_name] = []

    def add_event(self, action_name, event):
        action_name = action_name.lower()
        events = self.actions.get(action_name)
        if events is None:
            possible = ','.join(list(self.actions))
            raise UndefinedActionException("Undefined action {}. Possible values: {}".format(action_name, possible))

        events.append(event)

    def get_action(self, action_name):
        action_name = action_name.lower()
        return self.actions.get(action_name)

    def run_action(self, context, action_name):
        action_name = action_name.lower()
        # TODO: retornar steps aos inves de executar. Assim nao precisa conhecer context.
        events, parameters = self.__match_action(action_name)
        if events is None:
            possible = ','.join(list(self.actions))
            raise UndefinedActionException("Undefined action {}. Possible values: {}".format(action_name, possible))

        assert events is not None
        steps_to_run = ''
        for event in events:
            step_event = self.__replace_parameters(event, parameters)
            steps_to_run += step_event + '\n'

        context.execute_steps(steps_to_run)

    def __match_action(self, action_name):
        action_name = action_name.lower()
        for action_type in self.actions.keys():
            r = parse(action_type, action_name)
            if r:
                return self.actions[action_type], r.named

        return None, None

    def __replace_parameters(self, step, parameters):
        for parameter, value in parameters.items():
            token_to_find = "{" + parameter + "}"
            step = step.replace(token_to_find, value)

        return step


class DuplicatedActionException(Exception):
    pass


class UndefinedActionException(Exception):
    pass
