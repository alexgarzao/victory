# import os
# from time import gmtime, sleep, strftime
from time import sleep

from features.support.module import Module
from .support.windesk_driver import WindeskDriver


class WindeskModule(Module):
    def __init__(self, context):
        super().__init__('windesk', context)
        self.driver = WindeskDriver()
        # self.driver.chrome_driver_path = ("./chromedriver/chromedriver")

    def before_all(self):
        self.__load_steps()

    def __load_steps(self):
        import sys
        sys.path.insert(0, "windesk_features")
        import steps  # noqa: F401

    # def after_scenario(self, scenario):
    #     if self._context.failed:
    #         log = './output/LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
    #         screen_name = self.__get_screenshot(scenario, "FALHA")
    #         message = "\nFeature:{}\n   Linha em que falhou:{}\n   Screenshot:{}\n\n".format(
    #                 scenario.filename,
    #                 scenario.line,
    #                 screen_name
    #         )
    #         print(message)
    #
    #         with open(log, 'a') as arq:
    #             arq.write(message)
    #     else:
    #         if self._context.config_scenario:
    #             return
    #         screen_name = self.__get_screenshot(scenario, "SUCESSO")

    def after_step(self, step):
        if self._context.config_scenario:
            return

        sleep_time = self._context.test_config.get_number('SLEEP_BETWEEN_STEPS')
        if sleep_time > 0:
            sleep(sleep_time/1000)

    def after_all(self):
        if self.driver:
            self.driver.quit()

    # def get_unused_definitions(self):
    #     result = []
    #
    #     unused_screens = self.driver.get_unused_screens()
    #     if unused_screens:
    #         result.append(("Screens", [screen.name for screen in unused_screens]))
    #
    #     unused_elements = self.driver.get_unused_elements()
    #     if unused_elements:
    #         result.append(("Elements", [element.get_complete_name() for element in unused_elements]))
    #
    #     unused_actions = self.driver.get_unused_actions()
    #     if unused_actions:
    #         result.append(("Actions", unused_actions))
    #
    #     return result

    # def __get_screenshot(self, scenario, state):
    #     tags = ''
    #     tag_list = scenario.feature.tags + scenario.tags
    #
    #     if tag_list:
    #         tags += ','.join(tag_list) + '-'
    #
    #     screen_name = self.driver.screenshot(
    #             '{}-{}CENARIO: {}-Linha:{}'.format(
    #                     state,
    #                     tags,
    #                     os.path.basename(scenario.name),
    #                     scenario.line
    #             )
    #     )
    #
    #     return screen_name

    def start(self):
        server = self._context.test_config.get_string("SERVER")
        app = self._context.test_config.get_string("BINARY")

        self.driver.open(server, app)
