import subprocess


class BehaveRun:
    def __init__(self, features_path):
        self.features_path = features_path

    def run(self):
        behave_args = [
                "behave",
                "-D", "features_path={}/".format(self.features_path),
                "./features", "@{}/order.featureset".format(self.features_path),
                "--stop",
                "--format", "pretty",
                "--outfile", "/dev/stdout",
                "--format", "json.pretty",
                "--outfile", "{}/test_result.json".format(self.features_path),
                ]
        subprocess.run(behave_args)
