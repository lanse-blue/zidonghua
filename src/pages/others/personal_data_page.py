from selenium.webdriver.common.by import By
from src.pages.base_page import *


class PersonalDataPage(BasePage):
    change_pwd_btn_ele = (By.ID, "pwd")
    # iframe_ele = (By.XPATH,'//*[contains(@src, "Update")]')
    iframe_ele = (By.XPATH,'(//iframe)[2]')
    def click_change_pwd_btn(self):
        BasePage.switch_into_frame(self, self.iframe_ele)
        BasePage.find_element_explicitly(self, self.change_pwd_btn_ele).click()
