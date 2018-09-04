import os
import shutil

from test_suite import TestSuite


class TfsPull:
    def __init__(self, tfs, features_path):
        self.tfs = tfs
        self.features_path = features_path

    def run(self):
        testsuites = self.tfs.get_testsuites()

        self.__create_tfs_features_path(self.features_path)
        self.__create_tfs_features_path(self.features_path + '/custom_steps')

        with open(self.features_path + '/sequence.featureset', 'w') as f:
            for testsuite in testsuites:
                ts = TestSuite(self.tfs, testsuite)
                new_filename = ts.write_feature_file(self.features_path)
                f.write(new_filename + '\n')

        f.close()

    def __create_tfs_features_path(self, directory):
        try:
            shutil.rmtree(directory, ignore_errors=True)
            os.makedirs(directory)
        except OSError:
            assert False, "Failing when trying to create the {} directory...".format(directory)
