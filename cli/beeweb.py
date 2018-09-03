import click

from tfs_list import TfsList
from tfs_pull import TfsPull
# from tfs_update import TfsUpdate
from tfs_report import TfsReport
from tfs_integration import TfsIntegration
from tfs_config import TfsConfig
from report_config import ReportConfig
from webdriver_update import WebDriverUpdate
from behave_run import BehaveRun


TFS_FEATURES_PATH = "./tfs/"


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
@click.option('--url', prompt=True)
@click.option('--area-path', prompt=True)
@click.option('--user', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
@click.pass_context
def tfsconfig(ctx, url, area_path, user, password):
    tfs_config = TfsConfig("./config.ini", "TFS")
    tfs_config.update(url, area_path, user, password)


@cli.command()
@click.pass_context
def tfslist(ctx):
    # click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
    tfs_list = TfsList(__get_tfs_connection())
    tfs_list.run()


@cli.command()
@click.pass_context
def tfspull(ctx):
    tfs_pull = TfsPull(__get_tfs_connection(), TFS_FEATURES_PATH)
    tfs_pull.run()


@cli.command()
@click.pass_context
@click.argument('path')
def run(ctx, path):
    behave_run = BehaveRun(path)
    behave_run.run()


# @cli.command()
# @click.pass_context
# def update(ctx):
#     tfs_update = TfsUpdate(__get_tfs_connection())
#     tfs_update.run()


@cli.command()
@click.pass_context
def send_report(ctx):
    config = ReportConfig("./config.ini", "REPORT")
    config.read()

    tfs_report = TfsReport(config.smtp_server(), config.smtp_username(), config.smtp_password())
    tfs_report.send_by_email(
            smtp_from=config.smtp_from(),
            smtp_to=config.smtp_to(),
            project_name=config.project_name(),
            build_id=123,
            branch_name='XXXYYYZZZ',
            last_commit='XXXYYYZZZ',
    )


def __get_tfs_connection():
    config = TfsConfig("./config.ini", "TFS")
    config.read()

    tfs = TfsIntegration(config.url(), config.area_path(), config.user(), config.password())
    return tfs


def main():
    cli(obj={})


if __name__ == '__main__':
    main()
