import platform

from test_config import TestConfig
from time import gmtime, strftime, sleep

from web_app import WebApp


def before_all(context):
    context.config = TestConfig()
    context.config.driver = WebApp()
    os = platform.system().lower()
    context.config.driver.chrome_driver_path = ("./chromedriver/%s/chromedriver" % os)


def after_scenario(context, scenario):
    if context.failed:
        log = 'LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
        name_screen = context.config.driver.screenshot()
        message = "\nFeature:{}\n   Linha em que falhou:{}\n   Screenshot:{}\n\n".format(scenario.filename, scenario.line, name_screen)
        print(message)

        with open(log, 'a') as arq:
            arq.write(message)


def after_step(context, step):
    sleep_time = context.config.get_number('SLEEP_BETWEEN_STEPS')
    if sleep_time > 0:
        sleep(sleep_time/1000)


def after_all(context):
    if context.config.driver:
        context.config.driver.quit()


# ----------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ----------------------------------------------------------------------------
from behave import register_type

import parse
import parse_type


# @parse.with_pattern(r"\d+")
def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)
register_type(Number=parse_number)
