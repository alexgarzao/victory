import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from features.queries import Queries
from web_features.screens import Screens
from features.files import Files


class WebApp:
    def __init__(self):
        self.driver = None
        self.chrome_driver_path = None
        self.screens = Screens(None)
        self.current_screen = None
        self.queries = Queries()
        self.files = Files()
        self.retries = 10

    def open(self, headless, files_path):
        self.files.path = files_path

        self.chrome_driver_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_driver_options.add_argument('headless')
            self.chrome_driver_options.add_argument('no-sandbox')
            self.chrome_driver_options.add_argument('disable-gpu')

        # self.chrome_driver_options.add_argument('test-type')
        # self.chrome_driver_options.add_argument("disable-popup-blocking");
        self.chrome_driver_options.add_argument("incognito")
        self.chrome_driver_options.add_argument("disable-default-apps")
        self.chrome_driver_options.add_argument("disable-infobars")
        self.chrome_driver_options.add_argument("disable-extensions")

        ##############
        # self.chrome_driver_options.add_argument("no-sandbox")
        # self.chrome_driver_options.add_argument("disable-impl-side-painting")
        # self.chrome_driver_options.add_argument("disable-setuid-sandbox")
        # self.chrome_driver_options.add_argument("disable-seccomp-filter-sandbox")
        # self.chrome_driver_options.add_argument("disable-breakpad")
        # self.chrome_driver_options.add_argument("disable-client-side-phishing-detection")
        # self.chrome_driver_options.add_argument("disable-cast")
        # self.chrome_driver_options.add_argument("disable-cast-streaming-hw-encoding")
        # self.chrome_driver_options.add_argument("disable-cloud-import")
        # self.chrome_driver_options.add_argument("disable-popup-blocking")
        # self.chrome_driver_options.add_argument("ignore-certificate-errors")
        # self.chrome_driver_options.add_argument("disable-session-crashed-bubble")
        # self.chrome_driver_options.add_argument("disable-ipv6")
        # self.chrome_driver_options.add_argument("allow-http-screen-capture")
        self.chrome_driver_options.add_argument("start-maximized")
        #############

        preferences = {
                "download.default_directory": files_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
        }
        self.chrome_driver_options.add_experimental_option("prefs", preferences)

        # Try to find in "./chromedriver/" first.
        if os.path.exists(self.chrome_driver_path):
            self.driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.chrome_driver_options)
        else:
            self.driver = webdriver.Chrome(chrome_options=self.chrome_driver_options)

        self.driver.implicitly_wait(30)

        self.screens = Screens(self.driver)

    def quit(self):
        if self.driver:
            self.driver.quit()

    def url_assert_equal(self, url):
        for i in range(0, self.retries):
            try:
                current_url = self.driver.current_url[-len(url):]
                assert current_url == url
                return
            except AssertionError:
                time.sleep(1)
        assert False, 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada: {}'.format(
                current_url,
                url
        )

    def url_assert_start_with(self, start_url):
        for i in range(0, self.retries):
            try:
                current_url = self.driver.current_url[0:len(start_url)]
                assert current_url == start_url
                return
            except AssertionError:
                time.sleep(1)
        assert False, 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada: {}'.format(
                current_url,
                start_url
        )

    def follow_new_window(self):
        new_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to_window(new_window_handle)

    def return_previous_window(self):
        previous_window_handle = self.driver.window_handles[-2]
        self.driver.switch_to_window(previous_window_handle)

    def switch_to_frame(self, frame_name):
        frame = self.current_screen.find_element(frame_name)
        self.driver.switch_to_frame(frame)

    def switch_to_default(self):
        self.driver.switch_to_default_content()

    def screen_assert_equal(self, screen_name):
        screen = self.screens.get(screen_name)
        url = screen.get_url()

        self.__wait_for_ajax()

        # TODO: ainda eh necessario o retry abaixo?
        # for i in range(0, self.retries):
        for i in range(0, 1):
            try:
                current_url = self.driver.current_url[0:len(url)]
                assert current_url == url
                self.current_screen = screen
                return
            except AssertionError:
                time.sleep(1)
        assert False, 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada na tela {}: {}'.format(
                current_url,
                screen_name, url
        )

    def open_screen(self, screen_name):
        screen = self.screens.get(screen_name)
        url = screen.get_url()
        self.driver.get(url)
        self.current_screen = screen

    # def fill_value_by_name(self, field, value):
    #     el = self.driver.find_element_by_name(field)
    #     self.__fill_value(el, value)
    #
    # def __fill_value(self, el, value):
    #     el.send_keys(value + Keys.TAB)
    #     set_value = el.get_attribute('value')
    #     assert set_value == value

    def search_text(self, elemento):
        value = elemento.get_attribute('value')
        if value is None:
            value = elemento.text
        return value

    def find_element(self, component_name):
        element = self.current_screen.find_element(component_name)
        return element.find_element()

    def screenshot(self, file_prefix):
        path = os.getcwd()+'/output/screenshots/'+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())+"-"+file_prefix+".png"
        self.driver.save_screenshot(path)
        return path

    def new_screen(self, name):
        screen = self.screens.add(name)
        self.current_screen = screen
        return screen

    def new_action(self, action_name):
        self.current_screen.actions.new_action(action_name)

    def add_event_in_action(self, action_name, event):
        self.current_screen.actions.add_event(action_name, event)

    def run_action(self, context, action_name):
        self.current_screen.actions.run_action(context, action_name)

    def add_file(self, id, filename):
        self.files.add(id, filename)

    def get_filename(self, id):
        return self.files.get_filename(id)

    # TODO: Duplicated code :-/
    def __wait_for_ajax(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
            wait.until(lambda driver: self.driver.execute_script('return document.readyState == "complete"'))
        except Exception as e:
            pass
