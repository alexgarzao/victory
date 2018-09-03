import subprocess


class BehaveRun:
    def __init__(self, features_path):
        self.features_path = features_path

    def run(self):
        behave_args = [
                "behave",
                "-D", "features_path={}/".format(self.features_path),
                "./features", "@{}/sequence.featureset".format(self.features_path),
                "--stop",
                "--format", "pretty",
                "--outfile", "/dev/stdout",
                "--format", "json.pretty",
                "--outfile", "./output/test_result.json",
                ]
        subprocess.run(behave_args)
