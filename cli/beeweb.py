import configparser
import click
import subprocess

from tfs_list import TfsList
from tfs_pull import TfsPull
# from tfs_update import TfsUpdate
from tfs_report import TfsReport
from tfs_integration import TfsIntegration
from webdriver_update import WebDriverUpdate


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug


@cli.command()
@click.pass_context
def drivertest(ctx):
    webdriver = WebDriverUpdate()

    print("Installed release: {} Latest release: {}".format(webdriver.installed_release(), webdriver.latest_release()))

    if not webdriver.has_update():
        print("WebDriver already updated!")
        return

    print("WebDriver update available!")


@cli.command()
@click.pass_context
def driverupdate(ctx):
    webdriver = WebDriverUpdate()

    print("Installed release: {} Latest release: {}".format(webdriver.installed_release(), webdriver.latest_release()))

    if not webdriver.has_update():
        print("WebDriver already updated!")
        return

    webdriver.update()

    print("Installed release: {} Latest release: {}".format(webdriver.installed_release(), webdriver.latest_release()))
    print("WebDriver downloaded!")


@cli.command()
@click.pass_context
def list(ctx):
    # click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
    tfs_list = TfsList(__get_tfs_connection())
    tfs_list.run()


@cli.command()
@click.pass_context
def pull(ctx):
    tfs_pull = TfsPull(__get_tfs_connection())
    tfs_pull.run()


@cli.command()
@click.pass_context
def run(ctx):
    tfs_features_path = "./tfs_temp_features/"
    behave_args = [
            "behave",
            "-D", "features_path={}/".format(tfs_features_path),
            "./features", "@{}/order.featureset".format(tfs_features_path),
            "--stop",
            "--format", "pretty",
            "--outfile", "/dev/stdout",
            "--format", "json.pretty",
            "--outfile", "{}/test_result.json".format(tfs_features_path),
            ]
    subprocess.run(behave_args)


# @cli.command()
# @click.pass_context
# def update(ctx):
#     tfs_update = TfsUpdate(__get_tfs_connection())
#     tfs_update.run()


@cli.command()
@click.pass_context
def send_report(ctx):
    report_config = ctx.obj['config']['REPORT']
    smtp_server = report_config['SMTP_SERVER']
    smtp_from = report_config['FROM']
    smtp_to = report_config['TO']
    smtp_username = report_config['USERNAME']
    smtp_password = report_config['PASSWORD']
    project_name = report_config['PROJECT_NAME']

    tfs_report = TfsReport(__get_tfs_connection(), smtp_server, smtp_username, smtp_password)
    tfs_report.send_by_email(
            smtp_from=smtp_from,
            smtp_to=smtp_to,
            project_name=project_name,
            build_id=123,
            branch_name='XXXYYYZZZ',
            last_commit='XXXYYYZZZ',
    )


def __get_tfs_connection():
    config = configparser.ConfigParser(interpolation=None)
    config.read('./config.ini')

    tfs_user = config['TFS']['USER']
    tfs_password = config['TFS']['PASSWORD']
    tfs_url = config['TFS']['URL']
    tfs_area_path = config['TFS']['AREA_PATH']

    tfs = TfsIntegration(tfs_url, tfs_user, tfs_password, tfs_area_path)
    return tfs


def __get_config():
    config = configparser.ConfigParser(interpolation=None)
    config.read('./config.ini')

    return config


def main():
    cli(obj={'config': __get_config()})


if __name__ == '__main__':
    main()
