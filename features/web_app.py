from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os


class WebApp:
    def __init__(self, components):
        self.driver = None
        self.app = None
        self.chrome_driver_path = None
        self.components = components

    def open(self, headless):
        self.chrome_driver_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_driver_options.add_argument('headless')
            self.chrome_driver_options.add_argument('no-sandbox')

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
        component = self.components.get_component(component_name)

        if component.type == component.ID:
            element = self.find_element_by_xpath('//*[@id="' + component.internal_id + '"]')
        elif component.type == component.TEXT:
            element = self.find_element_by_xpath('//*[text()='+ component.internal_id +']')
        elif component.type == component.NAME:
            element = self.find_element_by_name(component.internal_id)
        elif component.type == component.XPATH:
            element = self.find_element_by_xpath(component.internal_id)
        elif component.type == component.AUTOMATION_ID:
            element = self.find_element_by_xpath('//*[@data-automation-id="' + component.internal_id + '"]')
        else:
            assert False, 'Invalid component type'

        assert element != None, 'Componente "%s" nao encontrado' % component.internal_id
        return element

    def find_element_by_xpath(self, xpath):
        return self.__try_to_get_element(self.driver.find_element_by_xpath, xpath)

    def find_element_by_id(self, id):
        return self.__try_to_get_element(self.driver.find_element_by_id, id)

    def find_element_by_name(self, name):
        return self.__try_to_get_element(self.driver.find_element_by_name, name)

    def find_element_by_automation_id(self, id):
        return self.__try_to_get_element(self.driver.find_element_by_xpath, id)

    def screenshot(self):
        path = os.getcwd()+'/print_erros/'+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())+".png"
        self.driver.save_screenshot(path)
        return path

    def __try_to_get_element(self, func, parameter):
        for retries in range(0, 5):
            el = func(parameter)
            if el and el.is_displayed: # and el.is_enabled:
                return el
            time.sleep(1)
        return None
