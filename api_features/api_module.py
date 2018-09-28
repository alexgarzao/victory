from time import gmtime, strftime

from features.support.module import Module
from .support.api_driver import ApiDriver


class ApiModule(Module):
    def __init__(self, context):
        super().__init__('api', context)
        self.driver = ApiDriver()

    def before_all(self):
        self.__load_steps()

    def __load_steps(self):
        import sys
        sys.path.insert(0, "api_features")
        import steps  # noqa: F401

    def after_scenario(self, scenario):
        if self._context.failed:
            log = './output/LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
            message = "\nFeature:{}\n   Linha em que falhou:{}\n\n".format(
                    scenario.filename,
                    scenario.line
            )
            print(message)

            with open(log, 'a') as arq:
                arq.write(message)
        else:
            if self._context.config_scenario:
                return

    def start(self):
        self.driver.set_base_url(self._context.test_config.get_string('BASE_URL'))
