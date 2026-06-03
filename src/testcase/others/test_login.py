from selenium import webdriver
from src.common import read_csv
from src.business.others import login_business


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get(read_csv.readcsv_obj.read_config_data('url.csv')['url'])

    def teardown_method(self):
        self.driver.quit()

    def test_login01(self):
        login_business.LoginBusiness(self.driver).login_hospital(1)

    def test_login02(self):
        login_business.LoginBusiness(self.driver).login_hospital(2)


if __name__ == '__main__':
    TestLogin().test_login01()
    TestLogin().test_login02()
