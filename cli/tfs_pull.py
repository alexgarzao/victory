from test_suite import TestSuite


class TfsPull:
    def __init__(self, tfs):
        self.tfs = tfs

    def run(self):
        testsuites = self.tfs.get_testsuites()

        for testsuite in testsuites:
            ts = TestSuite(self.tfs, testsuite)
            ts.write_feature_file('./temp/')
