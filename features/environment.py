import os
import shutil

from behave import register_type

from support.config import Config


def before_all(context):
    context.module = __choose_module_class(context, context.config.userdata['module'])
    context.module.before_all()

    __load_custom_steps(context)

    context.test_config = Config()

    # TODO: mover para o modulo
    __create_dir('./output/screenshots/')


def __choose_module_class(context, module):
    if module == 'web':
        from web_features.web_module import WebModule
        return WebModule(context)
    elif module == 'api':
        from api_features.api_module import ApiModule
        return ApiModule(context)
    else:
        assert False, "Undefined module {}".format(module)


def before_scenario(context, scenario):
    context.config_scenario = False


def after_scenario(context, scenario):
    context.module.after_scenario(scenario)


def after_step(context, step):
    context.module.after_step(step)


def after_all(context):
    context.module.after_all()


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
