from selenium import webdriver
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

    def teardown_method(self):
        self.driver.quit()

    def test_change_pwd(self):
        self.change_pwd_bussniess_obj.change_pwd_click_btn(1)

    def test_change_pwd02(self):
        self.change_pwd_bussniess_obj.change_pwd_click_btn(2)


if __name__ == '__main__':
    TestChangePwd().test_change_pwd()
    TestChangePwd().test_change_pwd02()
