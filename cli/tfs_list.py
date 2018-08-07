from work_item import WorkItem


class TfsList:
    def __init__(self, tfs):
        self.tfs = tfs

    def run(self):
        print('Listagem de todos os testsuites do projeto (com seus testcases):')
        testsuites = self.tfs.get_testsuites()

        for testsuite in testsuites:
            print('\nTestSuite:', testsuite['id'], testsuite['title'])

            testcases = self.tfs.get_testcases_from_testsuite(testsuite['id'])

            for testcase in testcases:
                wi = WorkItem(testcase)
                print('\n')
                print(wi.to_scenario())
                print('\n')

        print('Fim da listagem')
