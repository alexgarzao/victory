import os
import shutil

from behave import register_type

from config import Config
from time import gmtime, strftime, sleep

from web_features.web_driver import WebDriver


def before_all(context):
    __load_web_steps(context)
    __load_custom_steps(context)

    context.test_config = Config()
    context.driver = WebDriver()
    context.driver.chrome_driver_path = ("./chromedriver/chromedriver")

    __create_dir('./output/screenshots/')


def before_scenario(context, scenario):
    context.config_scenario = False


def after_scenario(context, scenario):
    if context.failed:
        log = './output/LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
        screen_name = __get_screenshot(context.driver, scenario, "FALHA")
        message = "\nFeature:{}\n   Linha em que falhou:{}\n   Screenshot:{}\n\n".format(
                scenario.filename,
                scenario.line,
                screen_name
        )
        print(message)

        with open(log, 'a') as arq:
            arq.write(message)
    else:
        if context.config_scenario:
            return
        screen_name = __get_screenshot(context.driver, scenario, "SUCESSO")


def __get_screenshot(webdriver, scenario, state):
    tags = ''
    tag_list = scenario.feature.tags + scenario.tags

    if tag_list:
        tags += ','.join(tag_list) + '-'

    screen_name = webdriver.screenshot(
            '{}-{}CENARIO: {}-Linha:{}'.format(
                    state,
                    tags,
                    os.path.basename(scenario.name),
                    scenario.line
            )
    )

    return screen_name


def after_step(context, step):
    if context.config_scenario:
        return

    sleep_time = context.test_config.get_number('SLEEP_BETWEEN_STEPS')
    if sleep_time > 0:
        sleep(sleep_time/1000)


def after_all(context):
    if context.driver:
        context.driver.quit()


def __load_web_steps(context):
    import sys
    sys.path.insert(0, "web_features")
    import steps  # noqa: F401


def __load_custom_steps(context):
    userdata = context.config.userdata
    features_path = userdata.get("features_path", "")
    if features_path and os.path.isdir(features_path + "/custom_steps"):
        import sys
        sys.path.insert(0, features_path)
        import custom_steps  # noqa: F401


def __create_dir(directory):
    try:
        shutil.rmtree(directory, ignore_errors=True)
        os.makedirs(directory)
    except OSError:
        assert False, "Failing when trying to create the {} directory...".format(directory)


# ----------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ----------------------------------------------------------------------------
def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)
register_type(Number=parse_number)  # noqa: E305
