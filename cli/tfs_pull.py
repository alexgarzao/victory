from test_suite import TestSuite


class TfsPull:
    def __init__(self, tfs):
        self.tfs = tfs

    def run(self):
        testsuites = self.tfs.get_testsuites()

        with open('./tfs_temp_features/order.featureset', 'w') as f:
            for testsuite in testsuites:
                ts = TestSuite(self.tfs, testsuite)
                new_filename = ts.write_feature_file('./tfs_temp_features/')
                f.write(new_filename + '\n')

        f.close()
