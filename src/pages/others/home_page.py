from selenium import webdriver
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class HomePage(BasePage):
    home_bg_ele = (By.XPATH, '(//*[text()="后台首页"])[2]')
    username_ele = (By.CSS_SELECTOR, '[class="adminName"]+span')
    personal_data_ele = (By.CSS_SELECTOR, '#userInfo dd:first-child cite')
    outpatient_mgt_ele = (By.XPATH, '//*[text()="门诊管理"]')
    user_reg_ele = (By.XPATH, '//*[text()="用户挂号"]')

    def hover_over_username(self):
        BasePage.hover_over_element(self, BasePage.find_element_explicitly(self, self.username_ele))

    def click_personal_data_btn(self):
        BasePage.find_element_explicitly(self, self.personal_data_ele).click()

    def get_text_of_home_bg(self):
        return BasePage.find_element_explicitly(self, self.home_bg_ele).text

    def click_outpatient_mgt(self):
        BasePage.find_element_explicitly(self, self.outpatient_mgt_ele).click()

    def click_user_reg(self):
        BasePage.find_element_explicitly(self, self.user_reg_ele).click()
