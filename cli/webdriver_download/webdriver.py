import click

from webdriver_update import WebDriverUpdate


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug


@cli.command()
@click.pass_context
def test(ctx):
    webdriver = WebDriverUpdate()

    print("Installed release: {} Latest release: {}".format(webdriver.installed_release(), webdriver.latest_release()))

    if not webdriver.has_update():
        print("WebDriver already updated!")
        return

    print("WebDriver update available!")


@cli.command()
@click.pass_context
def update(ctx):
    webdriver = WebDriverUpdate()

    print("Installed release: {} Latest release: {}".format(webdriver.installed_release(), webdriver.latest_release()))

    if not webdriver.has_update():
        print("WebDriver already updated!")
        return

    webdriver.update()

    print("Installed release: {} Latest release: {}".format(webdriver.installed_release(), webdriver.latest_release()))
    print("WebDriver downloaded!")


def main():
    cli(obj={})


if __name__ == '__main__':
    main()
