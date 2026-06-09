from time import sleep

from src.common.read_csv import *
from src.pages.others.home_page import HomePage
from src.pages.mzgl.user_reg_page import *
from src.pages.mzgl.add_patient_page import *


class UserRegBusiness(UserRegPage, AddPatientPage):
    def user_reg(self, row_num):
        case_data = readcsv_obj.read_case_data('user_reg_case_data.csv', row_num)
        home_page_obj = HomePage(self.driver)
        home_page_obj.click_outpatient_mgt()
        home_page_obj.click_user_reg()
        UserRegPage.click_plus_btn(self)
        if case_data[0] != '':
            AddPatientPage.input_patient_name(self, case_data[0])
            if case_data[1] == '女':
                AddPatientPage.choose_female(self)
            if case_data[2]:
                AddPatientPage.input_patient_age(self, case_data[2])
                if case_data[3]:
                    AddPatientPage.input_patient_phone(self, case_data[3])

                    if case_data[4]:
                        AddPatientPage.input_patient_card_id(self, case_data[4])

                        if case_data[5]:
                            AddPatientPage.select_dept(self, case_data[5])

                            if case_data[6]:
                                AddPatientPage.select_reg_type(self, case_data[6])
                                if case_data[7]:
                                    AddPatientPage.select_doctor(self, case_data[7])
        AddPatientPage.click_submit_btn(self)


if __name__ == '__main__':
   pass