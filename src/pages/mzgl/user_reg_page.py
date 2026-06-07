from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class UserRegPage(BasePage):
    plus_btn_ele = (By.CSS_SELECTOR, '.xiang > span')
    iframe_ele = (By.XPATH,'//*[contains(@src,"cao")]')
    def click_plus_btn(self):
        BasePage.switch_into_frame(self, self.iframe_ele)
        BasePage.find_element_explicitly(self, self.plus_btn_ele).click()