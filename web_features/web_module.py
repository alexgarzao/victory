import os
from time import gmtime, sleep, strftime

from features.module import Module
from .support.web_driver import WebDriver


class WebModule(Module):
    def __init__(self, context):
        super().__init__('web', context)
        self.driver = WebDriver()
        self.driver.chrome_driver_path = ("./chromedriver/chromedriver")

    def before_all(self):
        self.__load_steps()

    def __load_steps(self):
        import sys
        sys.path.insert(0, "web_features")
        import steps  # noqa: F401

    def after_scenario(self, scenario):
        if self.context.failed:
            log = './output/LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
            screen_name = self.__get_screenshot(scenario, "FALHA")
            message = "\nFeature:{}\n   Linha em que falhou:{}\n   Screenshot:{}\n\n".format(
                    scenario.filename,
                    scenario.line,
                    screen_name
            )
            print(message)

            with open(log, 'a') as arq:
                arq.write(message)
        else:
            if self.context.config_scenario:
                return
            screen_name = self.__get_screenshot(scenario, "SUCESSO")

    def after_step(self, step):
        if self.context.config_scenario:
            return

        sleep_time = self.context.test_config.get_number('SLEEP_BETWEEN_STEPS')
        if sleep_time > 0:
            sleep(sleep_time/1000)

    def after_all(self):
        if self.context.module.driver:
            self.context.module.driver.quit()

    def __get_screenshot(self, scenario, state):
        tags = ''
        tag_list = scenario.feature.tags + scenario.tags

        if tag_list:
            tags += ','.join(tag_list) + '-'

        screen_name = self.driver.screenshot(
                '{}-{}CENARIO: {}-Linha:{}'.format(
                        state,
                        tags,
                        os.path.basename(scenario.name),
                        scenario.line
                )
        )

        return screen_name

    def start(self):
        features_path = self.context.test_config.get_string("FEATURES_PATH")
        path = features_path + "/" + self.context.test_config.get_string('FILES_PATH')
        headless = self.context.test_config.get_bool('HEADLESS')

        if headless:
            self.context.test_config.set('SLEEP_BETWEEN_STEPS', 0)

        self.context.module.driver.open(headless, path)
