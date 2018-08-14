import json
from prettytable import PrettyTable


class TfsUpdate:
    def __init__(self, tfs):
        self.tfs = tfs

    def run(self):
        with open('./tfs_temp_features/test_result.json', 'r') as f:
            test_result = json.load(f)

        f.close()

        result_work_item = self.__create_or_get_result_work_item()

        table = PrettyTable()

        table.field_names = ["US", "Outcome", "ID", "Title"]

        for feature_result in test_result:
            for scenario in feature_result['elements']:
                table.add_row(["999", scenario['status'], "999", scenario['name']])
                # self.__update_testcase_status(scenario['name'], scenario['status'])

        print(table)
        result_work_item['description'] = table.get_html_string()


    # def __update_testcase_status(self, scenario_name, status):
    #     test_case_id = int(scenario_name.split(' ')[-1])
    #     test_case = self.tfs.get_workitem(test_case_id)
    #     # print(test_case['state'])
    #     test_case['state'] = 'Closed' # New, Active, CustomState, Resolved, Closed

    def __create_or_get_result_work_item(self):
        work_item = self.tfs.get_work_item_by_title('Resultado do Test Suite 999') # TODO: Deveria ter o ID do test suite
        if work_item is None:
            work_item = self.__create_result_work_item()

        return work_item

    def __create_result_work_item(self):
        testsuites = self.tfs.get_testsuites()
        assert len(testsuites) > 0

        # TODO: e se tiver mais de uma testsuite?
        testsuite = testsuites[0]
        testcases = self.tfs.get_testcases_from_testsuite(testsuite['id'])

        assert len(testcases) > 0

        testcase = testcases[0]
        new_wi = self.tfs.client.copy_workitem(testcase, with_links_and_attachments=True)
        new_wi['Title'] = 'Resultado do Test Suite 999'
        new_wi['Description'] = 'TODO'
        return new_wi
