import configparser
import click

from tfs_pull import TfsPull
from tfs_integration import TfsIntegration


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug

@cli.command()
@click.pass_context
def pull(ctx):
    config = configparser.ConfigParser(interpolation=None)
    config.read('./config.ini')

    tfs_user = config['TFS']['USER']
    tfs_password = config['TFS']['PASSWORD']
    tfs_url = config['TFS']['URL']
    tfs_area_path = config['TFS']['AREA_PATH']

    tfs = TfsIntegration(tfs_url, tfs_user, tfs_password, tfs_area_path)

    tfs_pull = TfsPull(tfs)
    tfs_pull.run()


if __name__ == '__main__':
    cli(obj={})
