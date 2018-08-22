from screen import *


class Screens:
    def __init__(self, driver):
        self.driver = driver
        self.screens = {}
        self.current_screen = None

    def add(self, screen_name):
        if self.screens.get(screen_name) != None:
            raise DuplicatedScreenException("Screen {} already exists".format(screen_name))

        screen = Screen(self.driver)
        self.screens[screen_name] = screen

        return screen

    def get(self, screen_name):
        screen = self.screens.get(screen_name)
        if screen is None:
            possible = ','.join(list(self.screens))
            raise ScreenNotFoundException("Screen {} not found. Possible values: {}".format(screen_name, possible))

        return screen


class DuplicatedScreenException(Exception):
    pass


class ScreenNotFoundException(Exception):
    pass
