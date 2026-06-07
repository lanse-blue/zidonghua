import pymysql
from pymysql import MySQLError

from src.common.read_csv import *


class ConnectMysql:
    def __init__(self):
        # 连接数据库
        self.conn_mysql_obj = pymysql.connect(host=readcsv_obj.read_config_data('db_info.csv')['host'],
                                              user=readcsv_obj.read_config_data('db_info.csv')['username'],
                                              password=readcsv_obj.read_config_data('db_info.csv')['password'],
                                              port=int(readcsv_obj.read_config_data('db_info.csv')['port']),
                                              database=readcsv_obj.read_config_data('db_info.csv')['db'],
                                              charset='utf8')
        self.cursor = self.conn_mysql_obj.cursor()

    def fetch_one_result(self, dql):
        if self.conn_mysql_obj and self.cursor:
            self.cursor.execute(dql)
            return self.cursor.fetchone()
        else:
            print('数据库连接失败')

    def execute_dml(self, dml):
        try:
            if self.conn_mysql_obj and self.cursor:
                self.cursor.execute(dml)
                self.conn_mysql_obj.commit()
        except MySQLError:
            print('数据库操作失败')
            self.conn_mysql_obj.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn_mysql_obj:
            self.conn_mysql_obj.close()


if __name__ == '__main__':
    print(ConnectMysql().fetch_one_result('select pwd,salt from sys_user;'))
