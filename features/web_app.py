from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os

from element import IdElement, TextElement, NameElement, XpathElement, AutomationIdElement, ClassNameElement


class WebApp:
    def __init__(self):
        self.driver = None
        self.app = None
        self.chrome_driver_path = None
        self.elements = {}
        self.screens = {}

    def open(self, headless):
        self.chrome_driver_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_driver_options.add_argument('headless')
            self.chrome_driver_options.add_argument('no-sandbox')

        self.chrome_driver_options.add_argument('test-type')
        self.chrome_driver_options.add_argument("disable-popup-blocking");
        self.chrome_driver_options.add_argument("incognito");
        self.chrome_driver_options.add_argument("disable-default-apps");
        self.chrome_driver_options.add_argument("disable-infobars");
        self.chrome_driver_options.add_argument("disable-extensions");

        ##############
        self.chrome_driver_options.add_argument("no-sandbox")
        self.chrome_driver_options.add_argument("disable-impl-side-painting")
        self.chrome_driver_options.add_argument("disable-setuid-sandbox")
        self.chrome_driver_options.add_argument("disable-seccomp-filter-sandbox")
        self.chrome_driver_options.add_argument("disable-breakpad")
        self.chrome_driver_options.add_argument("disable-client-side-phishing-detection")
        self.chrome_driver_options.add_argument("disable-cast")
        self.chrome_driver_options.add_argument("disable-cast-streaming-hw-encoding")
        self.chrome_driver_options.add_argument("disable-cloud-import")
        self.chrome_driver_options.add_argument("disable-popup-blocking")
        self.chrome_driver_options.add_argument("ignore-certificate-errors")
        self.chrome_driver_options.add_argument("disable-session-crashed-bubble")
        self.chrome_driver_options.add_argument("disable-ipv6")
        self.chrome_driver_options.add_argument("allow-http-screen-capture")
        self.chrome_driver_options.add_argument("start-maximized")
        #############

        self.driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.chrome_driver_options)
        self.driver.get(self.app)
        self.driver.implicitly_wait(30)

    def quit(self):
        if self.driver:
            self.driver.quit()

    def url_assert_equal(self, url):
        for i in range(0, 20):
            try:
                current_url = self.driver.current_url[-len(url):]
                assert current_url == url
                return
            except:
                time.sleep(1)
        assert False , 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada: {}'.format(current_url, url)

    def url_assert_start_with(self, start_url):
        for i in range(0, 20):
            try:
                current_url = self.driver.current_url[0:len(start_url)]
                assert current_url == start_url
                return
            except:
                time.sleep(1)
        assert False , 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada: {}'.format(current_url, start_url)

    def screen_assert_equal(self, screen):
        url = self.screens[screen]
        for i in range(0, 5):
            try:
                current_url = self.driver.current_url[0:len(url)]
                assert current_url == url
                return
            except:
                time.sleep(1)
        assert False , 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada na tela {}: {}'.format(current_url, screen, url)

    def open_screen(self, screen):
        url = self.screens[screen]
        self.driver.get(url)

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

    def find_element(self, component_name):
        self.__wait_for_ajax()
        return self.elements[component_name].find_element()

    def __wait_for_ajax(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(lambda driver: self.driver.execute_script("return jQuery.active == 0"))
            wait.until(lambda driver: self.driver.execute_script('return document.readyState == "complete"'))
        except Exception as e:
            pass

    def screenshot(self):
        path = os.getcwd()+'/print_erros/'+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())+".png"
        self.driver.save_screenshot(path)
        return path

    def clear_elements(self):
        self.elements.clear()

    def new_id_element(self, name, internal_id):
        self.elements[name] = IdElement(self.driver, name, internal_id)

    def new_text_element(self, name, internal_id):
        self.elements[name] = TextElement(self.driver, name, internal_id)

    def new_name_element(self, name, internal_id):
        self.elements[name] = NameElement(self.driver, name, internal_id)

    def new_xpath_element(self, name, internal_id):
        self.elements[name] = XpathElement(self.driver, name, internal_id)

    def new_automation_id_element(self, name, internal_id):
        self.elements[name] = AutomationIdElement(self.driver, name, internal_id)

    def new_class_name_element(self, name, class_name):
        self.elements[name] = ClassNameElement(self.driver, name, class_name)

    def new_screen(self, name, url):
        self.screens[name] = url
