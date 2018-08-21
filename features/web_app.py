from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os

from element import IdElement, TextElement, NameElement, XpathElement, AutomationIdElement, ClassNameElement
from actions import Actions
from queries import Queries


class WebApp:
    def __init__(self):
        self.driver = None
        self.chrome_driver_path = None
        self.elements = {}
        self.screens = {}
        self.actions = Actions()
        self.current_screen = ''
        self.queries = Queries()
        self.retries = 5

    def open(self, headless):
        self.chrome_driver_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_driver_options.add_argument('headless')
            self.chrome_driver_options.add_argument('no-sandbox')

        # self.chrome_driver_options.add_argument('test-type')
        # self.chrome_driver_options.add_argument("disable-popup-blocking");
        self.chrome_driver_options.add_argument("incognito");
        self.chrome_driver_options.add_argument("disable-default-apps");
        self.chrome_driver_options.add_argument("disable-infobars");
        self.chrome_driver_options.add_argument("disable-extensions");

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

        self.driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.chrome_driver_options)
        self.driver.implicitly_wait(30)

    def quit(self):
        if self.driver:
            self.driver.quit()

    def url_assert_equal(self, url):
        for i in range(0, self.retries):
            try:
                current_url = self.driver.current_url[-len(url):]
                assert current_url == url
                return
            except:
                time.sleep(1)
        assert False , 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada: {}'.format(current_url, url)

    def url_assert_start_with(self, start_url):
        for i in range(0, self.retries):
            try:
                current_url = self.driver.current_url[0:len(start_url)]
                assert current_url == start_url
                return
            except:
                time.sleep(1)
        assert False , 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada: {}'.format(current_url, start_url)

    def screen_assert_equal(self, screen_name):
        url = self.__get_screen_url(screen_name)
        for i in range(0, self.retries):
            try:
                current_url = self.driver.current_url[0:len(url)]
                assert current_url == url
                self.current_screen = screen_name
                return
            except:
                time.sleep(1)
        assert False , 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada na tela {}: {}'.format(current_url, screen_name, url)

    def open_screen(self, screen_name):
        url = self.__get_screen_url(screen_name)
        self.driver.get(url)
        self.current_screen = screen_name

    def __get_screen_url(self, screen_name):
        url = self.screens.get(screen_name)
        if url is None:
            possible = ','.join(list(self.screens))
            raise ScreenNotFoundException("Screen {} not found. Possible values: {}".format(screen_name, possible))

        return url

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
        if value == None:
            value = elemento.text
        return value

    def set_current_screen(self, screen_name):
        self.current_screen = screen_name

    def find_element(self, component_name):
        element = self.elements.get(self.__get_element_name(component_name))
        if element is None:
            elements_without_prefix = [element.split('/')[1] for element in self.elements]
            possible = ','.join(list(elements_without_prefix))
            raise ElementNotFoundException("Element {} not found. Possible values: {}".format(component_name, possible))

        self.__wait_for_ajax()
        return element.find_element()

    def __wait_for_ajax(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
            wait.until(lambda driver: self.driver.execute_script('return document.readyState == "complete"'))
        except Exception as e:
            pass

    def screenshot(self, file_prefix):
        path = os.getcwd()+'/screenshots/'+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())+"-"+file_prefix+".png"
        self.driver.save_screenshot(path)
        return path

    def clear_elements(self):
        self.elements.clear()

    def __add_element(self, name, new_element):
        internal_name = self.__get_element_name(name)
        if self.elements.get(internal_name) != None:
            raise DuplicatedElementException("Element {} already exists".format(name))

        self.elements[internal_name] = new_element

    def new_id_element(self, name, internal_id):
        self.__add_element(name, IdElement(self.driver, name, internal_id))

    def new_text_element(self, name, internal_id):
        self.__add_element(name, TextElement(self.driver, name, internal_id))

    def new_name_element(self, name, internal_id):
        self.__add_element(name, NameElement(self.driver, name, internal_id))

    def new_xpath_element(self, name, internal_id):
        self.__add_element(name, XpathElement(self.driver, name, internal_id))

    def new_automation_id_element(self, name, internal_id):
        self.__add_element(name, AutomationIdElement(self.driver, name, internal_id))

    def new_class_name_element(self, name, class_name):
        self.__add_element(name, ClassNameElement(self.driver, name, class_name))

    def new_screen(self, name, url):
        if self.screens.get(name) != None:
            raise DuplicatedScreenException("Screen {} already exists".format(name))

        self.screens[name] = url

    def new_action(self, action_name):
        self.actions.new_action(self.__get_element_name(action_name))

    def add_event_in_action(self, action_name, event):
        self.actions.add_event(self.__get_element_name(action_name), event)

    def run_action(self, context, action_name):
        self.actions.run_action(context, self.__get_element_name(action_name))

    def __get_element_name(self, element_name):
        return self.current_screen + '/' + element_name


class DuplicatedElementException(Exception):
    pass


class DuplicatedScreenException(Exception):
    pass


class ScreenNotFoundException(Exception):
    pass


class ElementNotFoundException(Exception):
    pass
