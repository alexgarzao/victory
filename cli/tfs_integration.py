from tfs import TFSAPI
from requests_ntlm import HttpNtlmAuth # Use NTLM authorization


class TfsIntegration:
    def __init__(self, tfs_url, user, password, project):
        self.project = project
        self.client = TFSAPI(
            tfs_url,
            project=project,
            user=user,
            password=password,
            auth_type=HttpNtlmAuth)
             #, connect_timeout=10, read_timeout=30

    def get_workitem(self, workitem_id):
        return self.client.get_workitem(workitem_id)

    def get_workitems(self):
        ## NOTE: Fields in SELECT really ignored, wiql return Work Items with all fields
        query = """SELECT
            [System.Id],
            [System.WorkItemType],
            [System.Title],
            [System.ChangedDate]
        FROM workitems
        WHERE
            [System.AreaPath] = '{}'
        ORDER BY [System.Title]""".format(self.project)
        # ORDER BY [System.ChangedDate]""".format(self.project)

        wiql = self.client.run_wiql(query)

        # Get founded Work Item ids
        # ids = wiql.workitem_ids

        return wiql.workitems

    def get_testcases(self):
        query = """SELECT
            [System.Id],
            [System.WorkItemType],
            [System.Title],
            [System.ChangedDate]
        FROM workitems
        WHERE
            [System.WorkItemType] = 'Test Case' AND
            [System.AreaPath] = '{}'
        ORDER BY [System.Title]""".format(self.project)

        wiql = self.client.run_wiql(query)
        return wiql.workitems

    def get_testcases_from_testsuite(self, test_suite_id):
        test_suite = self.get_workitem(test_suite_id)
        assert test_suite['WorkItemType'] == 'User Story'

        testcases = []
        for relation in test_suite.data['relations']:
            if relation['rel'] == 'Microsoft.VSTS.Common.TestedBy-Forward':
                workitem_id = self.__get_workitem_id_from_url(relation['url'])
                testcases.append(self.get_workitem(workitem_id))

        # Order by title
        testcases = sorted(testcases, key=lambda testcase: testcase['Title'])
        return testcases

    def get_work_item_by_title(self, title):
        query = """SELECT
            [System.Id],
            [System.WorkItemType],
            [System.Title],
            [System.ChangedDate]
        FROM workitems
        WHERE
            [System.AreaPath] = '{}' AND
            [System.Title] = '{}'""".format(self.project, title)

        workitems = self.client.run_wiql(query).workitems
        assert len(workitems) <= 1
        if len(workitems) == 0:
            return None

        return workitems[0]

    @staticmethod
    def __get_workitem_id_from_url(url):
        # Example:
        # 'url':'https://tfs.e-unicred.com.br/Unicred/70711659-4c4f-4ac0-965c-ae87fbae6d49/_apis/wit/workItems/45327'
        workitem_id = int(url.split('/')[-1])
        return workitem_id

    def get_testcases_from_current_sprint(self):
        query = """SELECT
            [System.Id],
            [System.WorkItemType],
            [System.Title],
            [System.ChangedDate]
        FROM workitems
        WHERE
            [System.WorkItemType] = 'Test Case' AND
            [System.AreaPath] = '{}' AND
            [System.IterationPath] = @CurrentIteration
        ORDER BY [System.Title]""".format(self.project)

        wiql = self.client.run_wiql(query)
        return wiql.workitems

    def get_testsuites(self):
        query = """
        SELECT
            *
        FROM
            workitems
        WHERE
            [System.WorkItemType] = 'User Story' AND
            [System.AreaPath] = '{}' AND
            [Related Link Count] >= 1
        ORDER BY
            [System.Title]""".format(self.project)

        wiql = self.client.run_wiql(query)
        workitems = wiql.workitems

        # Filter for relations.rel = Microsoft.VSTS.Common.TestedBy-Forward
        # (Pdb) www = [workitem for workitem in workitems if {'rel':'Microsoft.VSTS.Common.TestedBy-Forward'} in workitem.data['relations']]
        filtered = set()
        for workitem in workitems:
            for relation in workitem.data['relations']:
                if relation['rel'] == 'Microsoft.VSTS.Common.TestedBy-Forward':
                    filtered.add(workitem)

        return list(filtered)
