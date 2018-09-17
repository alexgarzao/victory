import subprocess
import os

import click


class BehaveRun:
    def run(self, module, features_path, debug, stop_on_error, tags, headless):
        if not os.path.isdir(features_path):
            click.secho("Features path '{}' not found!".format(features_path), fg='red')
            exit(1)

        behave_args = [
                "behave",
                "-D", "features_path={}/".format(features_path),
                "-D", "module={}".format(module),
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

        if headless:
            behave_args.append("-D")
            behave_args.append("headless")

        result = subprocess.run(behave_args)
        return result.returncode
