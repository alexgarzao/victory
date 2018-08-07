from work_item import WorkItem


class TestSuite:
    def __init__(self, tfs, test_suite):
        self.tfs = tfs
        self.test_suite = test_suite

    def write_feature_file(self, path_dir='./'):
        test_suite = self.test_suite
        filename = '{}/TestSuite {}: {}.feature'.format(path_dir, test_suite['id'], test_suite['title'])

        with open(filename, 'w') as f:
            f.write("Funcionalidade: {}\n".format(test_suite['title']))

            testcases = self.tfs.get_testcases_from_testsuite(test_suite['id'])

            for testcase in testcases:
                wi = WorkItem(testcase)
                f.write('\n' + wi.to_scenario() + '\n')

        f.close()
