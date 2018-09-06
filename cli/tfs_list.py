import click

from work_item import WorkItem


class TfsList:
    def __init__(self, tfs):
        self.tfs = tfs

    def run(self):
        # print('Listagem de todos os testsuites do projeto:')
        # workitems = self.tfs.get_testsuites()
        #
        # for workitem in workitems:
        #     print(workitem['id'], workitem['title'])
        #
        # print('Fim da listagem\n\n')
        #
        # print('Listagem de todos os testcases do projeto:')
        # workitems = self.tfs.get_testcases()
        #
        # for workitem in workitems:
        #     wi = WorkItem(workitem)
        #     print('\n')
        #     print(wi.to_scenario())
        #     print('\n')
        # print('Fim da listagem\n\n')
        #
        click.echo('Listagem de todos os testsuites do projeto (com seus testcases):')
        testsuites = self.tfs.get_testsuites()

        for testsuite in testsuites:
            click.echo('\nTestSuite:{} {}'.format(testsuite['id'], testsuite['title']))

            testcases = self.tfs.get_testcases_from_testsuite(testsuite['id'])

            for testcase in testcases:
                wi = WorkItem(testcase)
                click.echo('\n')
                click.echo(wi.to_scenario())
                click.echo('\n')

        click.echo('Fim da listagem')
