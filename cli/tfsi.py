import configparser
import click
import subprocess

from tfs_list import TfsList
from tfs_pull import TfsPull
from tfs_update import TfsUpdate
from tfs_integration import TfsIntegration


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug


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
    behave_args = ["behave", "-D", "features_path={}/".format(tfs_features_path), "./features", "@{}/order.featureset".format(tfs_features_path), "--stop", "--format", "json.pretty", "--outfile", "{}/test_result.json".format(tfs_features_path)]
    subprocess.run(behave_args)


@cli.command()
@click.pass_context
def update(ctx):
    tfs_update = TfsUpdate(__get_tfs_connection())
    tfs_update.run()


def __get_tfs_connection():
    config = configparser.ConfigParser(interpolation=None)
    config.read('./config.ini')

    tfs_user = config['TFS']['USER']
    tfs_password = config['TFS']['PASSWORD']
    tfs_url = config['TFS']['URL']
    tfs_area_path = config['TFS']['AREA_PATH']

    tfs = TfsIntegration(tfs_url, tfs_user, tfs_password, tfs_area_path)
    return tfs


def main():
    cli(obj={})

if __name__ == '__main__':
    main()
