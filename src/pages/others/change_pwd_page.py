from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class ChangePwdPage(BasePage):
    old_pwd_ele = (By.ID, "jpwd")
    new_pwd_ele = (By.ID, "pwd1")
    confirm_pwd_ele = (By.ID, "pwd2")
    save_btn_ele = (By.ID, "qwe")
    cancle_btn_ele = (By.ID, "guanbi")
    close_btn_ele = (By.CLASS_NAME, "layui-layer-close")

    def input_pwd(self, old_pwd, new_pwd, confirm_pwd):
        """

        :param old_pwd:
        :param new_pwd:
        :param confirm_pwd:
        :return:
        """
        BasePage.find_element_explicitly(self, self.old_pwd_ele).send_keys(old_pwd)
        BasePage.find_element_explicitly(self, self.new_pwd_ele).send_keys(new_pwd)
        BasePage.find_element_explicitly(self, self.confirm_pwd_ele).send_keys(confirm_pwd)

    def click_save_btn(self):
        BasePage.find_element_explicitly(self, self.save_btn_ele).click()

    def click_cancle_btn(self):
        BasePage.find_element_explicitly(self, self.cancle_btn_ele).click()

    def click_close_btn(self):
        BasePage.find_element_explicitly(self, self.close_btn_ele).click()
