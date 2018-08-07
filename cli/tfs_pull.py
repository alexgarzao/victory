from bs4 import BeautifulSoup


class TfsPull:
    def __init__(self, tfs):
        self.tfs = tfs

    def run(self):
        # click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))

        print('Listagem de todos os testsuites do projeto:')
        workitems = self.tfs.get_testsuites()

        for workitem in workitems:
            print(workitem['id'], workitem['title'])

        print('Fim da listagem\n\n')

        print('Listagem de todos os testcases do projeto:')
        workitems = self.tfs.get_testcases()

        for workitem in workitems:
            print(workitem['id'], workitem['title'])
            print(workitem['description'])
            print('\n\n\n')
            print(self.__convert_description_to_scenario(workitem['description']))
            print('\n\n\n')
        print('Fim da listagem\n\n')

        print('Listagem de todos os testsuites do projeto (com seus testcases):')
        testsuites = self.tfs.get_testsuites()

        for testsuite in testsuites:
            print('TestSuite:', testsuite['id'], testsuite['title'])

            testcases = self.tfs.get_testcases_from_testsuite(testsuite['id'])

            for testcase in testcases:
                print('TestCase:', testcase['id'], testcase['title'])
                print(self.__convert_description_to_scenario(testcase['description']))
                print('\n\n\n')

        print('Fim da listagem\n\n')

    @staticmethod
    def __convert_description_to_scenario(description):
        soup = BeautifulSoup(description, "html.parser")
        return soup.get_text('\n')
