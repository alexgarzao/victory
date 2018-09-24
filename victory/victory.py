import click

from tfs_list import TfsList
from tfs_pull import TfsPull
# from tfs_update import TfsUpdate
from report import Report
from tfs_integration import TfsIntegration
from tfs_config import TfsConfig
from report_config import ReportConfig
from webdriver_update import WebDriverUpdate
from behave_run import BehaveRun


TFS_FEATURES_PATH = "./tfs/"


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('--stop-on-error/--dont-stop-on-error', default=False)
@click.pass_context
def cli(ctx, debug, stop_on_error):
    ctx.obj['DEBUG'] = debug
    ctx.obj['STOP-ON-ERROR'] = stop_on_error


@cli.command()
@click.pass_context
def drivertest(ctx):
    webdriver = WebDriverUpdate()

    click.echo(
        "Installed release: {} Latest release: {}".format(webdriver.installed_release(), webdriver.latest_release()))

    if not webdriver.has_update():
        click.echo("WebDriver already updated!")
        return

    click.echo("WebDriver update available!")


@cli.command()
@click.pass_context
def driverupdate(ctx):
    webdriver = WebDriverUpdate()

    click.echo("Installed release: {} Latest release: {}".format(
        webdriver.installed_release(), webdriver.latest_release()))

    if not webdriver.has_update():
        click.echo("WebDriver already updated!")
        return

    webdriver.update()

    click.echo("Installed release: {} Latest release: {}".format(
        webdriver.installed_release(), webdriver.latest_release()))
    click.echo("WebDriver downloaded!")


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
@click.argument('module')
@click.argument('path')
@click.argument('scenarios', nargs=-1, required=False)
@click.option('--tags', multiple=True)
@click.option('--headless/--no-headless', default=False)
def run(ctx, module, path, scenarios, tags, headless):
    behave_run = BehaveRun()
    status_code = behave_run.run(module, path, scenarios, ctx.obj['DEBUG'], ctx.obj['STOP-ON-ERROR'], tags, headless)
    if status_code:
        exit(status_code)


# @cli.command()
# @click.pass_context
# def update(ctx):
#     tfs_update = TfsUpdate(__get_tfs_connection())
#     tfs_update.run()


@cli.command()
@click.pass_context
def sendreport(ctx):
    config = ReportConfig("./config.ini", "REPORT")
    config.read()

    report = Report(config.smtp_server(), config.username(), config.password())
    report.send_by_email(
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
