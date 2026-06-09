from selenium import webdriver

from src.business.mzgl.user_reg_business import UserRegBusiness
from src.business.others.login_business import LoginBusiness
from src.common.read_csv import *
from src.common.connect_mysql import *


class TestUserReg:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        url = readcsv_obj.read_config_data('url.csv')['url']
        self.driver.get(url)
        LoginBusiness(self.driver).login_hospital(1)
        mysql_obj = ConnectMysql()
        dml = "delete from report where `state` = 1;"
        mysql_obj.execute_dml(dml)
        mysql_obj.close()
        self.user_reg_business_obj = UserRegBusiness(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_user_reg_patientname_is_2_characters(self):
        try:
            self.user_reg_business_obj.user_reg(2)
            data = readcsv_obj.read_case_data('user_reg_case_data.csv', 2)
            expected_name = data[0]
            expected_phone = data[3]
            actual_name = self.user_reg_business_obj.get_text_of_patientname()
            actual_phone = self.user_reg_business_obj.get_text_of_phone()
            assert expected_name == actual_name
            assert expected_phone == actual_phone
            mysql_obj = ConnectMysql()
            dql = f"select reportid from report where reportName='{expected_name}' and phone='{expected_phone}' and state = 1 ;"
            actual_report_id = mysql_obj.fetch_one_result(dql)[0]
            mysql_obj.close()
            expected_report_id = int(self.user_reg_business_obj.get_text_of_reportid())
            assert actual_report_id == expected_report_id
        except:
            self.user_reg_business_obj.get_screenshot('用例异常')
            raise

    def test_user_reg_patientname_is_empty(self):
        try:
            self.user_reg_business_obj.user_reg(3)
            expected_result = self.user_reg_business_obj.get_text_of_prompt()
            actual_result = '必填项不能为空'
            assert actual_result == expected_result
            actual_patientname_class_value = self.user_reg_business_obj.get_class_of_patient_name()
            expected_patientname_class_value = 'layui-form-danger'
            assert expected_patientname_class_value in actual_patientname_class_value
        except:
            self.user_reg_business_obj.get_screenshot('用例异常')
            raise

    def test_user_reg_patientage_is_empty(self):
        try:
            self.user_reg_business_obj.user_reg(4)



        except:
            self.user_reg_business_obj.get_screenshot('用例异常')
            raise
if __name__ == '__main__':
    TestUserReg().test_user_reg_patientname_is_2_characters()