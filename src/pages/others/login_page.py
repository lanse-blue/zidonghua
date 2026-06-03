from src.common.read_csv import ReadCSV
from src.pages.base_page import *
from selenium import webdriver
class LoginPage(BasePage):
    username_ele = (By.ID, "loginname")
    password_ele = (By.ID, "pwd")
    login_button_ele = (By.CSS_SELECTOR, '[class="layui-btn layui-block"]')
    def login(self, username, password):
        BasePage.find_element_explicitly(self,self.username_ele).send_keys(username)
        BasePage.find_element_explicitly(self,self.password_ele).send_keys(password)
        BasePage.find_element_explicitly(self,self.login_button_ele).click()
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get(ReadCSV().read_config_data('url.csv')['url'])
    LoginPage(driver).login(ReadCSV().read_case_data('login_case_data.csv', 1),ReadCSV().read_case_data('login_case_data.csv', 2))