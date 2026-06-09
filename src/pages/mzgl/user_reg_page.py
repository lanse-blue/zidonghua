from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class UserRegPage(BasePage):
    plus_btn_ele = (By.CSS_SELECTOR, '.xiang > span')
    iframe_ele = (By.XPATH, '//*[contains(@src,"cao")]')
    name_ele = (By.CSS_SELECTOR, '#reall > div:nth-child(2) span')
    phone_ele = (By.CSS_SELECTOR, '#reall > div:nth-child(3) span')
    report_id_ele = (By.CSS_SELECTOR, '#reall > div:nth-child(1) span')
    def get_text_of_patientname(self):
        return BasePage.find_element_explicitly(self, self.name_ele).text

    def get_text_of_phone(self):
        return BasePage.find_element_explicitly(self, self.phone_ele).text
    def get_text_of_reportid(self):
        return BasePage.find_element_explicitly(self, self.report_id_ele).text

    def click_plus_btn(self):
        BasePage.switch_into_frame(self, self.iframe_ele)
        BasePage.find_element_explicitly(self, self.plus_btn_ele).click()
