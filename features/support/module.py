from features.support.actions import Actions
from features.support.variables import Variables
from features.support.queries import Queries
from features.support.simple_result import SimpleResult


class Module:
    def __init__(self, type, context):
        self.__type = type
        self._context = context
        self.__generic_actions = Actions()
        self.__variables = Variables()
        self.queries = Queries()

    def before_all(self):
        pass

    def before_feature(self, feature):
        pass

    def before_scenario(self, scenario):
        self.__run_special_tags(scenario.tags)

    def __run_special_tags(self, tags):
        special_tags = [s[8:] for s in tags if s.startswith('victory.')]
        for special_tag in special_tags:
            if special_tag.startswith('runonce.'):
                action = special_tag[8:]
                if self.__generic_actions.was_used(action):
                    continue
            elif special_tag.startswith('run.'):
                action = special_tag[4:]
            else:
                assert False, "Undefined special tag '{}'".format(special_tag)

            steps_to_execute = self.__generic_actions.get_steps_to_execute(action)
            self._context.execute_steps(steps_to_execute)

    def after_scenario(self, scenario):
        pass

    def after_step(self, step):
        pass

    def after_all(self):
        pass

    def get_unused_definitions(self):
        return None

    def add_generic_action(self, action_name):
        self.__generic_actions.add_action(action_name)

    def add_event_in_generic_action(self, action_name, event):
        self.__generic_actions.add_event(action_name, event)

    def get_steps_to_execute(self, action_name):
        return self.__generic_actions.get_steps_to_execute(action_name)

    def get_content(self, value):
        if type(value) != str or not value:
            return SimpleResult(value)

        if value.startswith("$query:"):
            query_name = value[7:]
            return self.queries.run(query_name)

        if value.startswith('$var:'):
            var = value[5:]
            return self.__variables.get_variable_result(var)

        if value.startswith('$'):
            raise Exception("Invalid $ tag: {}".format(value))

        return SimpleResult(value)

    def set_variable_result(self, variable, value):
        self.__variables.set_variable_result(variable, value)

    def get_variable_result(self, variable):
        return self.__variables.get_variable_result(variable)
