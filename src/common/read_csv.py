import os
import csv
from src.common.getpath import *


# 定义一个类，用来读取csv文件的数据（测试用例数据和配置数据）
class ReadCSV:

    def read_case_data(self, file_name, row_num):
        """
        :param file_name: 文件名
        :param row_num: 行数
        :return:返回的是需要测试的用例的数据，数据类型为列表
        """
        csv_path = os.path.join(get_path.get_data_path(), file_name)

        with open(csv_path, 'r', encoding='utf-8') as f:
            csv_data = csv.reader(f)
            print(csv_data, type(csv_data))
            data = list(csv_data)
        return data[row_num - 1]

    def read_config_data(self, file_name):
        """
        :param file_name: 文件名
        :param row_num: 行数
        :return:返回的是需要测试的用例的数据，数据类型为列表
        """
        csv_path = os.path.join(get_path.get_config_path(), file_name)
        with open(csv_path, 'r', encoding='utf-8') as f:
            csv_data = csv.reader(f)
            data = dict(csv_data)
        return data


readcsv_obj = ReadCSV()

if __name__ == '__main__':
    print(ReadCSV().read_case_data('login_case_data.csv', 1))
    print(ReadCSV().read_config_data('db_info.csv'))
