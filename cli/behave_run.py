import subprocess
import os
import sys

import click


class BehaveRun:
    def run(self, features_path, debug, stop_on_error, tags):
        if not os.path.isdir(features_path):
            click.secho("Features path '{}' not found!".format(features_path), fg='red')
            sys.exit()

        behave_args = [
                "behave",
                "-D", "features_path={}/".format(features_path),
                "./features", "@{}/sequence.featureset".format(features_path),
                "--format", "pretty",
                "--outfile", "/dev/stdout",
                "--format", "json.pretty",
                "--outfile", "./output/test_result.json",
                ]

        if debug:
            behave_args.append("--no-capture")

        if stop_on_error:
            behave_args.append("--stop")

        for tag in tags:
            behave_args.append("--tags={}".format(tag))

        subprocess.run(behave_args)
