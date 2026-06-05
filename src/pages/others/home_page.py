from selenium import webdriver
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class HomePage(BasePage):
    home_bg_ele = (By.XPATH, '(//*[text()="后台首页"])[2]')
    username_ele = (By.CSS_SELECTOR, '[class="adminName"]+span')
    personal_data_ele = (By.CSS_SELECTOR, '#userInfo dd:first-child cite')

    def hover_over_username(self):
        BasePage.hover_over_element(self, BasePage.find_element_explicitly(self, self.username_ele))

    def click_personal_data_btn(self):
        BasePage.find_element_explicitly(self, self.personal_data_ele).click()

    def get_text_of_home_bg(self):
        return BasePage.find_element_explicitly(self, self.home_bg_ele).text
