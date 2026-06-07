from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class AddPatientPage(BasePage):
    patient_name_ele = (By.CSS_SELECTOR, '[placeholder"请输入用户姓名"]')
    female_ele = (By.CSS_SELECTOR, '[value="女"] +')