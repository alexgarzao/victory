from bs4 import BeautifulSoup


class WorkItem:
    def __init__(self, tfs_work_item):
        self.tfs_work_item = tfs_work_item

    def to_scenario(self):
        scenario = "@TestCase.{}\n".format(self.tfs_work_item['id'])
        scenario += "Cenário: {} - TESTCASE ID: {}\n".format(self.tfs_work_item['title'], self.tfs_work_item['id'])
        scenario += self.__convert_description_to_text()
        return scenario

    def __convert_description_to_text(self):
        description = self.tfs_work_item['description']
        soup = BeautifulSoup(description, "html.parser")
        return soup.get_text('\n')
