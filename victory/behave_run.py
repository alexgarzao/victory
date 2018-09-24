import subprocess
import os

import click


class BehaveRun:
    def run(self, module, features_path, scenarios, debug, stop_on_error, tags, headless):
        if not os.path.isdir(features_path):
            click.secho("Features path '{}' not found!".format(features_path), fg='red')
            exit(1)

        if not scenarios:
            scenarios = ["."]

        behave_args = [
                "behave",
                "-D", "features_path={}/".format(features_path),
                "-D", "module={}".format(module),
                "--format", "pretty",
                "--outfile", "/dev/stdout",
                "--format", "json.pretty",
                "--outfile", "./output/test_result.json",
                "./features",
                "{}/setup/".format(features_path),
                ]

        for scenario in scenarios:
            behave_args.append("{}/scenarios/{}".format(features_path, scenario))

        if debug:
            behave_args.append("--no-capture")

        if stop_on_error:
            behave_args.append("--stop")

        for tag in tags:
            behave_args.append("--tags=setup,{}".format(tag))

        if headless:
            behave_args.append("-D")
            behave_args.append("headless")

        result = subprocess.run(behave_args)
        return result.returncode
