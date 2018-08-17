import platform
import os
import shutil

from test_config import TestConfig
from time import gmtime, strftime, sleep

from web_app import WebApp


def before_all(context):
    __load_custom_steps(context)

    context.config = TestConfig()
    context.config.driver = WebApp()
    os = platform.system().lower()
    context.config.driver.chrome_driver_path = ("./chromedriver/%s/chromedriver" % os)

    __create_screenshots_dir('./screenshots/')


def after_scenario(context, scenario):
    if context.failed:
        log = 'LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
        tags = ''
        if scenario.tags:
            tags = ' ' + ', '.join(scenario.tags) + ' -'
        name_screen = context.config.driver.screenshot('FALHA -{} ARQUIVO: {}:{} - '.format(tags, os.path.basename(scenario.filename), scenario.line))
        import pdb; pdb.set_trace()
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


def __load_custom_steps(context):
    userdata = context.config.userdata
    features_path = userdata.get("features_path", "")
    if features_path:
        import sys
        sys.path.insert(0, features_path)
        import custom_steps


def __create_screenshots_dir(directory):
    try:
        shutil.rmtree(directory, ignore_errors=True)
        os.makedirs(directory)
    except:
        assert False, "Failing when trying to create the {} directory...".format(directory)


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
