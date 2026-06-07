import os


class GetPath:
    def get_pro_path(self):
        cur_filepath = os.path.realpath(__file__)
        pro_path = os.path.dirname(os.path.dirname(os.path.dirname(cur_filepath)))
        return pro_path

    def get_data_path(self):
        data_path = os.path.join(self.get_pro_path(), 'data')
        return data_path

    def get_config_path(self):
        config_path = os.path.join(self.get_pro_path(), 'config')
        return config_path

    def get_pictures_path(self):
        picture_path = os.path.join(self.get_pro_path(), 'pictures')
        return picture_path

    def get_reports_path(self):
        reports_path = os.path.join(self.get_pro_path(), 'reports')
        return reports_path

    def get_testcase_path(self):
        testcase_path = os.path.join(self.get_pro_path(), 'testcase')
        return testcase_path

    def get_pages_path(self):
        pages_path = os.path.join(self.get_pro_path(), 'pages')
        return pages_path


get_path = GetPath()
