from time import gmtime, strftime

from features.module import Module
from api_features.api_driver import ApiDriver
from api_features.variables import Variables


class ApiModule(Module):
    # TODO: Nao seria melhor receber context no init?
    def __init__(self, context):
        super().__init__('api', context)
        self.driver = ApiDriver()
        self.variables = Variables()

    def before_all(self):
        self.__load_steps()

    def __load_steps(self):
        import sys
        sys.path.insert(0, "api_features")
        import steps  # noqa: F401

    def after_scenario(self, scenario):
        if self.context.failed:
            log = './output/LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
            message = "\nFeature:{}\n   Linha em que falhou:{}\n\n".format(
                    scenario.filename,
                    scenario.line
            )
            print(message)

            with open(log, 'a') as arq:
                arq.write(message)
        else:
            if self.context.config_scenario:
                return

    def start(self):
        self.driver.set_base_url(self.context.test_config.get_string('BASE_URL'))
