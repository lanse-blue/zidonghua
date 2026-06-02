import os
import csv


# 定义一个类，用来读取csv文件的数据（测试用例数据和配置数据）
class ReadCSV:
    def read_case_data(self, file_name):
        """
        :param file_name: 文件名
        :return:
        """
        cur_filepath = os.path.abspath(__file__)
        pro_path = os.path.dirname(os.path.dirname(os.path.dirname(cur_filepath)))
        csv_path = os.path.join(pro_path, 'data', file_name)
        print(csv_path)

        with open(csv_path, 'r', encoding='utf-8') as f:
            csv_data = csv.reader(f)
            print(csv_data,type(csv_data))
            data = list(csv_data)
        return data


if __name__ == '__main__':
    print(ReadCSV().read_case_data('login_case_data.csv'))
