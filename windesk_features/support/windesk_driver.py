import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium_based_drivers.screens import Screens


class WindeskDriver:
    def __init__(self):
        self.driver = None
        self.screens = Screens(None)
        self.__current_screen = None
        self.retries = 10

    def open(self, server, app):
        self.driver = webdriver.Remote(
            command_executor=server,
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app": app
            })

        self.driver.implicitly_wait(30)
        self.screens = Screens(self.driver)

    def quit(self):
        if self.driver:
            self.driver.quit()

    def follow_new_window(self):
        new_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to_window(new_window_handle)

    def return_previous_window(self):
        previous_window_handle = self.driver.window_handles[-2]
        self.driver.switch_to_window(previous_window_handle)

    def switch_to_frame(self, frame_name):
        frame = self.__current_screen.find_element(frame_name)
        self.driver.switch_to_frame(frame)

    def switch_to_default(self):
        self.driver.switch_to_default_content()

    def screen_assert_equal(self, screen_name):
        # TODO
        pass

    def open_screen(self, screen_name):
        screen = self.screens.get(screen_name)
        url = screen.get_url()
        self.driver.get(url)
        self.__current_screen = screen

    def search_text(self, elemento):
        value = elemento.get_attribute('value')
        if value is None:
            value = elemento.text
        return value

    def screenshot(self, file_prefix):
        path = os.getcwd() + '/output/screenshots/' + \
            time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) +\
            "-" + file_prefix + ".png"
        self.driver.save_screenshot(path)
        return path

    def add_screen(self, name):
        screen = self.screens.add(name)
        self.__current_screen = screen
        return screen

    def add_file(self, id, filename):
        self.files.add(id, filename)

    def get_filename(self, id):
        return self.files.get_filename(id)

    def get_current_screen(self):
        return self.__current_screen

    def get_unused_screens(self):
        return self.screens.get_unused_screens()

    def get_unused_elements(self):
        return self.screens.get_unused_elements()

    def get_unused_actions(self):
        return self.screens.get_unused_actions()

    # TODO: Duplicated code :-/
    def __wait_for_ajax(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
            wait.until(lambda driver: self.driver.execute_script('return document.readyState == "complete"'))
        except Exception as e:
            pass
