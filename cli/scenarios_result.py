import json
from prettytable import PrettyTable


class ScenariosResult:
    TESTCASE_TAG_PREFIX = "TestCase."

    def __init__(self):
        table = PrettyTable()
        table.field_names = ["História", "Status", "TestCase ID", "Título", "Tempo de execução"]

        test_result = self.__get_test_result()

        self.build_status = 'SUCESSO'
        self.total_features = 0
        self.failed_features = 0
        self.total_scenarios = 0
        self.failed_scenarios = 0
        self.duration = 0.0

        last_testcase_id = 0

        for feature_result in test_result:
            last_us_id = feature_result['tags'][0].split('.')[1]
            self.total_features += 1
            if feature_result['status'] == 'failed':
                self.build_status = 'FALHA'
                self.failed_features += 1

            for scenario in feature_result['elements']:
                last_testcase_id = self.__get_testcase_id(scenario['tags'], last_testcase_id)
                self.total_scenarios += 1
                if scenario['status'] == 'failed':
                    self.failed_scenarios += 1

                scenario_duration = self.__get_scenario_duration(scenario)
                self.duration += scenario_duration
                table.add_row([last_us_id, scenario['status'], last_testcase_id, scenario['name'], "{0:.2f}s".format(scenario_duration)])

        self.html_table = table.get_html_string(attributes={"border": "1"})

    def __get_test_result(self):
        with open('./tfs_temp_features/test_result.json', 'r') as f:
            test_result = json.load(f)

        f.close()

        return test_result

    def __get_testcase_id(self, tags, default_id):
        if len(tags) == 0:
            return default_id

        for tag in tags:
            if tag.startswith(ScenariosResult.TESTCASE_TAG_PREFIX):
                testcase_id = tag[len(ScenariosResult.TESTCASE_TAG_PREFIX):]
                return testcase_id

        return default_id

    def __get_scenario_duration(self, scenario):
        duration = 0.0
        for step in scenario['steps']:
            duration += step['result']['duration']

        return duration
