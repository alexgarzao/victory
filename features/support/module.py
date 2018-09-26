from features.support.actions import Actions


class Module:
    def __init__(self, type, context):
        self.type = type
        self.context = context
        self.generic_actions = Actions()

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
                if self.generic_actions.was_used(action):
                    continue
            elif special_tag.startswith('run.'):
                action = special_tag[4:]
            else:
                assert False, "Undefined special tag '{}'".format(special_tag)

            steps_to_execute = self.generic_actions.get_steps_to_execute(action)
            self.context.execute_steps(steps_to_execute)

    def after_scenario(self, scenario):
        pass

    def after_step(self, step):
        pass

    def after_all(self):
        pass

    def get_unused_definitions(self):
        return None

    def add_generic_action(self, action_name):
        self.generic_actions.add_action(action_name)

    def add_event_in_generic_action(self, action_name, event):
        self.generic_actions.add_event(action_name, event)

    def get_steps_to_execute(self, action_name):
        return self.generic_actions.get_steps_to_execute(action_name)
