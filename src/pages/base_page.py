from os.path import join

from selenium.webdriver import ActionChains

from src.common.getpath import *
from src.common.time_stamp import *
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
    def get_screenshot(self,case_title):
        """

        :param case_title:
        :return:
        """
        picture_abspath =join(get_path.get_pictures_path(),f"{case_title}_{get_cur_time()}.png")
        self.driver.get_screenshot_as_file(picture_abspath)
    def hover_over_element(self, element,pause_time = 2):
        """

        :param element:
        :param pause_time:
        :return:
        """
        action_chains_obj = ActionChains(self.driver)
        action_chains_obj.move_to_element(element).pause(pause_time).perform()
    def switch_into_frame(self,locator,timeout=5):
        wait_obj = WebDriverWait(self.driver, timeout)
        wait_obj.until(EC.frame_to_be_available_and_switch_to_it(locator))