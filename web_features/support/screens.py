from .screen import Screen


class Screens:
    def __init__(self, driver):
        self.driver = driver
        self.screens = {}
        self.current_screen = None

    def add(self, screen_name):
        screen_name = screen_name.lower()
        if self.screens.get(screen_name) is not None:
            raise DuplicatedScreenException("Screen {} already exists".format(screen_name))

        screen = Screen(self.driver, screen_name)
        self.screens[screen_name] = screen

        return screen

    def get(self, screen_name):
        screen_name = screen_name.lower()
        screen = self.screens.get(screen_name)
        if screen is None:
            possible = ','.join(list(self.screens))
            raise ScreenNotFoundException("Screen {} not found. Possible values: {}".format(screen_name, possible))

        screen.inc_uses_number()
        return screen

    def get_unused_screens(self):
        unused_screens = [screen for key, screen in self.screens.items() if screen.get_uses_number() == 0]
        return unused_screens

    def get_unused_elements(self):
        unused_elements = []
        for key, screen in self.screens.items():
            unused_elements += screen.get_unused_elements()

        return unused_elements

    def get_unused_actions(self):
        unused_actions = []
        for key, screen in self.screens.items():
            unused_actions += screen.get_unused_actions()

        return unused_actions


class DuplicatedScreenException(Exception):
    pass


class ScreenNotFoundException(Exception):
    pass
