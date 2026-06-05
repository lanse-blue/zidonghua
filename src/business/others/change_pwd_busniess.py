from time import sleep

from selenium import webdriver
from src.common.read_csv import readcsv_obj
from src.pages.others.home_page import *
from src.pages.others.personal_data_page import *
from src.pages.others.change_pwd_page import *
class ChangePwdBusiness(ChangePwdPage):
    def change_pwd_click_btn(self,row_num,btn_name="保存"):
        oldpwd,new_pwd,confirm_pwd = readcsv_obj.read_case_data('change_case_data.csv',row_num)
        home_page_obj = HomePage(self.driver)
        home_page_obj.hover_over_username()
        home_page_obj.click_personal_data_btn()
        sleep(2)
        PersonalDataPage(self.driver).click_change_pwd_btn()
        ChangePwdPage(self.driver).input_pwd(oldpwd,new_pwd,confirm_pwd)
        if btn_name == "保存":
            ChangePwdPage(self.driver).click_save_btn()
        elif btn_name == "取消":
            ChangePwdPage(self.driver).click_cancle_btn()
        elif btn_name == "关闭":
            ChangePwdPage(self.driver).click_close_btn()