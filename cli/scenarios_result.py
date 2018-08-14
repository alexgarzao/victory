import json
from prettytable import PrettyTable


class ScenariosResult:
    def __init__(self):
        table = PrettyTable()
        table.field_names = ["US", "Outcome", "ID", "Title"]

        test_result = self.__get_test_result()

        self.build_status = 'SUCESSO'
        self.total_features = 0
        self.failed_features = 0
        self.total_scenarios = 0
        self.failed_scenarios = 0

        for feature_result in test_result:
            last_us_id = feature_result['tags'][0].split('.')[1]
            self.total_features += 1
            if feature_result['status'] == 'failed':
                self.build_status = 'FALHA'
                self.failed_features += 1

            for scenario in feature_result['elements']:
                last_testcase_id = scenario['tags'][0].split('.')[1]
                self.total_scenarios += 1
                if scenario['status'] == 'failed':
                    self.failed_scenarios += 1

                table.add_row([last_us_id, scenario['status'], last_testcase_id, scenario['name']])

        self.html_table = table.get_html_string(attributes={"border":"1"})

    def __get_test_result(self):
        with open('./tfs_temp_features/test_result.json', 'r') as f:
            test_result = json.load(f)

        f.close()

        return test_result
