import subprocess


class BehaveStepsCatalog:
    def run(self, module):
        behave_args = [
                "behave",
                "-D", "module={}".format(module),
                "--format=steps.catalog",
                "-q", "--no-summary"
                ]

        result = subprocess.run(behave_args)
        return result.returncode
