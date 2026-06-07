from selenium import webdriver

from src.common.connect_mysql import ConnectMysql
from src.common.read_csv import readcsv_obj
from src.business.others.login_business import *
from src.business.others.change_pwd_busniess import *


class TestChangePwd:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get(readcsv_obj.read_config_data('url.csv')['url'])
        self.login_bussniess_obj = LoginBusiness(self.driver)
        self.change_pwd_bussniess_obj = ChangePwdBusiness(self.driver)
        self.login_bussniess_obj.login_hospital(2, 'preset_login_data.csv')
        self.username = read_csv.readcsv_obj.read_case_data('preset_login_data.csv', 2)[0]
        self.dql = f'select pwd,salt from sys_user where loginname  = "{self.username}";'
        self.mysql_obj = ConnectMysql ()
        self.old_pwd,self.old_salt = self.mysql_obj.fetch_one_result(self.dql)

    def teardown_method(self):
        self.driver.quit()
        dml = f'update sys_user set pwd = "{self.old_pwd}" ,salt = "{self.old_salt}" where loginname = "{self.username}"'
        self.mysql_obj.execute_dml(dml)
        self.mysql_obj.close()

    def test_change_pwd(self):
        try:
            self.change_pwd_bussniess_obj.change_pwd_click_btn(2)
            actual_result = self.change_pwd_bussniess_obj.get_change_pwd_sucess_text()
            assert "修改成功" == actual_result
            mysql_obj = ConnectMysql()
            pwd,salt = mysql_obj.fetch_one_result(self.dql)
            mysql_obj.close()
            assert pwd != self.old_pwd
            assert salt != self.old_salt
        except:
            self.change_pwd_bussniess_obj.get_screenshot("修改密码成功")
            raise


    def test_change_pwd02(self):
        try:
            self.change_pwd_bussniess_obj.change_pwd_click_btn(3,'取消')
            actual_result = self.change_pwd_bussniess_obj.check_cancelbtn_is_invisible()
            assert actual_result is True
            mysql_obj = ConnectMysql()
            pwd,salt = mysql_obj.fetch_one_result(self.dql)
            mysql_obj.close()
            assert pwd == self.old_pwd
            assert salt == self.old_salt
        except:
            self.change_pwd_bussniess_obj.get_screenshot("修改密码失败")
            raise



if __name__ == '__main__':
    TestChangePwd().test_change_pwd()
    TestChangePwd().test_change_pwd02()
