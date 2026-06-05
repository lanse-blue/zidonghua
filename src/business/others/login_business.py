from src.common import read_csv
from src.pages.others import login_page


class LoginBusiness(login_page.LoginPage):
    def login_hospital(self, row_num,file_name='login_case_data.csv'):
        username, password = read_csv.readcsv_obj.read_case_data(file_name, row_num)
        login_page.LoginPage.login(self, username, password)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get(read_csv.readcsv_obj.read_config_data('url.csv')['url'])
    LoginBusiness(driver).login_hospital(2)
