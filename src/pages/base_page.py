import selenium.webdriver.common.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        """

        :param driver:
        """
        self.driver = driver
    def find_element_explicitly(self, locator, timeout=5):
        """

        :param locator:接受一个元组（By.css,"css表达式"）
        :param timeout:
        :return: 返回定位到的元素
        """
        emt = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return emt