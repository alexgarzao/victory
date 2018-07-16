from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os

from elements import Elements


class WebApp:
    def __init__(self):
        self.driver = None
        self.app = None
        self.chrome_driver_path = None
        self.elements = None

    def open(self, headless):
        self.chrome_driver_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_driver_options.add_argument('headless')
            self.chrome_driver_options.add_argument('no-sandbox')

        self.driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.chrome_driver_options)
        self.driver.get(self.app)
        self.driver.implicitly_wait(30)
        self.elements = Elements(self.driver)

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

    def fill_value_by_name(self, field, value):
        el = self.driver.find_element_by_name(field)
        self.__fill_value(el, value)

    def __fill_value(self, el, value):
        el.send_keys(value + Keys.TAB)
        set_value = el.get_attribute('value')
        assert set_value == value

    def search_text(self, elemento):
        value = elemento.get_attribute('value')
        if value == None:
            value = elemento.text
        return value

    def find_element(self, component_name):
        return self.elements.get_element(component_name)

    def screenshot(self):
        path = os.getcwd()+'/print_erros/'+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())+".png"
        self.driver.save_screenshot(path)
        return path
