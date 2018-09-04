import subprocess
import os
import sys


class BehaveRun:
    def __init__(self, features_path, debug, stop_on_error):
        self.features_path = features_path
        self.debug = debug
        self.stop_on_error = stop_on_error

    def run(self):
        if not os.path.isdir(self.features_path):
            sys.exit("Features path '{}' not found!".format(self.features_path))

        behave_args = [
                "behave",
                "-D", "features_path={}/".format(self.features_path),
                "./features", "@{}/sequence.featureset".format(self.features_path),
                "--format", "pretty",
                "--outfile", "/dev/stdout",
                "--format", "json.pretty",
                "--outfile", "./output/test_result.json",
                ]

        if self.debug:
            behave_args.append("--no-capture")

        if self.stop_on_error:
            behave_args.append("--stop")

        subprocess.run(behave_args)
