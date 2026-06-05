from selenium import webdriver
from src.common import read_csv
from src.business.others import login_business
from src.pages.others.home_page import HomePage


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get(read_csv.readcsv_obj.read_config_data('url.csv')['url'])
        self.login_bussniess_obj = login_business.LoginBusiness(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_login01(self):
        try:
            self.login_bussniess_obj.login_hospital(1)
            actual_result = HomePage(self.driver).get_text_of_home_bg()
            assert "后台首页" == actual_result
        except:
            self.login_bussniess_obj.get_picture("使用正确的账号和密码登录成功")
            raise
    def test_login02(self):
        try:
            self.login_bussniess_obj.login_hospital(2)
            actual_result = self.login_bussniess_obj.get_text_of_login_failed()
            assert "用户名或密码错误，请重试！" == actual_result
        except:
            self.login_bussniess_obj.get_screenshot("使用错误的密码")
            raise


if __name__ == '__main__':
    TestLogin().test_login01()
    TestLogin().test_login02()
