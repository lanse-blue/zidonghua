from time import sleep

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


# 定义一个类，用来封装添加病人页面的元素定位表达式 以及 元素 对应的操作
# 而且该类要继承 BasePage 类
class AddPatientPage(BasePage):
    # 病人姓名
    patient_name_ele = (By.CSS_SELECTOR, '[placeholder="请输入用户姓名"]')
    # 性别女（性别男是默认的）
    female_ele = (By.CSS_SELECTOR, '[value="女"] + div > i')
    # 年龄
    patient_age_ele = (By.ID, "age")
    # 电话
    patient_phone_ele = (By.ID, "phon")
    # 身份证号
    patient_card_id_ele = (By.ID, "idcard")

    """
    科室、挂号类型、医生 是 非select标签的下拉框，操作的步骤：1、先点击展开下拉框  2、选择下拉框中的选项元素
    对于 下拉框元素来说 正常定位进行操作即可。
    但是，与下拉框中的选项元素来说，建议把元素的定位表达式 写在一个【字典】中。
    以 科室下拉框为例：{"内科": (By.ID, "id属性的值"), "外科": (By.NAME, "name属性的值")}
    """
    # 科室
    # =========== 科室下拉框元素 ============
    dept_ele = (By.CSS_SELECTOR, '#departmentId + div i')
    # =========== 科室下拉框中的选项元素 ======== 元素定位表达式 要写成 【字典】格式===
    dept_options_ele = {
        "内科": (By.XPATH, '//dd[text()="内科"]'),
        "骨科": (By.XPATH, '//dd[text()="骨科"]'),
        "儿科": (By.XPATH, '//dd[text()="儿科"]')
    }

    # 挂号类型
    # ========= 挂号类型下拉框元素 =========
    user_reg_ele = (By.CSS_SELECTOR, "#registeredId + div i")
    # ========== 挂号类型下框中的选项元素 ===== 定位表达式写成【字典】格式 ===========
    user_reg_options_ele = {
        "普通挂号": (By.XPATH, '//dd[text()="普通挂号"]'),
        "专家号": (By.XPATH, '//dd[text()="专家号"]')
    }

    # 医生
    # ======== 医生下拉框元素 ========
    doctor_ele = (By.CSS_SELECTOR, '#doctorId + div i')
    # ======= 医生下拉框中的选项元素 =====写成【字典格式】 =======
    doctor_options_ele = {
        "扁鹊": (By.XPATH, '//dd[text()="扁鹊"]'),
        "华佗": (By.XPATH, '//dd[text()="华佗"]')
    }

    # 提交按钮
    submit_btn_ele = (By.CSS_SELECTOR, '[lay-filter="doSubmit"]')
    # 重置按钮
    reset_btn_ele = (By.CSS_SELECTOR, '[lay-filter="doSubmit"] + button')
    # 关闭按钮
    close_btn_ele = (By.CLASS_NAME, "layui-layer-close")

    prompt_of_required_filed_is_empty_ele = (By.XPATH, '//*[text()="必填项不能为空"]')

    def get_text_of_prompt(self):
        return BasePage.find_element_explicitly(self, self.prompt_of_required_filed_is_empty_ele).text
    def get_class_of_patient_name(self):
        return BasePage.find_element_explicitly(self, self.patient_name_ele).get_attribute('class')
    """
    我们要封装元素对应的操作，因为添加病人页面每一个表单都是 【必填项】，所以，使用 等价类 来设计用例，有效：填写； 无效：不填。
    所以，为验证 有效：填；无效：不填，每一个元素的操作 都要单独封装，这样才能在 业务层 判断 用例数据是有效的还是 无效的。
    在 业务层 需要对每一个表单都做一个判断：
    if 姓名不为空:
        填写姓名
    else:
        不填写姓名
    """

    # 定义一个方法，用来实现输入 病人姓名
    def input_patient_name(self, patient_name):
        ele = super().find_element_explicitly(self.patient_name_ele)
        ele.click()
        ele.clear()
        ele.send_keys(patient_name)

    # 定义一个方法，用来实现选择 性别女
    def choose_female(self):
        super().find_element_explicitly(self.female_ele).click()

    # 定义一个方法，用来实现输入 病人年龄
    def input_patient_age(self, patient_age):
        super().find_element_explicitly(self.patient_age_ele).send_keys(patient_age)

    # 定义一个方法，用来实现输入 病人电话
    def input_patient_phone(self, patient_phone):
        super().find_element_explicitly(self.patient_phone_ele).send_keys(patient_phone)

    # 定义一个方法，用来实现输入 病人身份证号码
    def input_patient_card_id(self, patient_card_id):
        super().find_element_explicitly(self.patient_card_id_ele).send_keys(patient_card_id)

    # 定义一个方法，用来选择 科室
    def select_dept(self, dept_name):
        # 1、点击展开科室下拉框
        super().find_element_explicitly(self.dept_ele).click()
        # 2、选择科室下拉框中的选项元素
        super().find_element_explicitly(self.dept_options_ele[dept_name]).click()

    # 定义一个方法，用来选择 挂号类型
    def select_reg_type(self, reg_type):
        # 1、点击展开挂号类型下拉框
        super().find_element_explicitly(self.user_reg_ele).click()
        # 2、选择挂号类型下拉框中的选项元素
        super().find_element_explicitly(self.user_reg_options_ele[reg_type]).click()

    # 定义一个方法，用来选择 医生
    def select_doctor(self, doctor_name):
        import time
        time.sleep(2)
        # 1、点击展开医生下拉框
        super().find_element_explicitly(self.doctor_ele).click()
        # 2、选择医生下拉框中的选项元素
        super().find_element_explicitly(self.doctor_options_ele[doctor_name]).click()

    # 定义一个方法，用来点击 提交按钮
    def click_submit_btn(self):
        sleep(1)
        super().find_element_explicitly(self.submit_btn_ele).click()

    # 定义一个方法，用来点击 重置按钮
    def click_reset_btn(self):
        super().find_element_explicitly(self.reset_btn_ele).click()

    # 定义一个方法，用来点击 关闭按钮
    def click_close_btn(self):
        super().find_element_explicitly(self.close_btn_ele).click()


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()  # 打开浏览器
    driver.maximize_window()  # 浏览器最大化
    driver.get("http://172.21.5.151:8080/sel/toLogin")
    # ====== 登录 == 调用 登录业务层的代码 进行 登录 ====
    from src.business.others.login_business import LoginBusiness

    LoginBusiness(driver).login_hospital(1)  # 要登录成功，所以，行号要写 2
    # ========= 操作后台首页中的元素 ========
    from src.pages.others.home_page import HomePage

    home_page_obj = HomePage(driver)
    home_page_obj.click_outpatient_mgt()  # 点击了 门诊管理
    home_page_obj.click_user_reg()  # 点击了 用户挂号
    # ======== 进入到 用户挂号页面 点击 + 号 ========
    from src.pages.mzgl.user_reg_page import UserRegPage

    UserRegPage(driver).click_plus_btn()  # 点击了 +号
    # =========== 进入到了 添加病人页面 ===========
    obj = AddPatientPage(driver)
    obj.input_patient_name("skjdl")  # 病人姓名
    obj.choose_female()  # 选择性别女
    obj.input_patient_age(20)  # 输入了年龄
    obj.input_patient_phone(12345678965)
    obj.input_patient_card_id(610113202606072003)
    obj.select_dept("内科")
    obj.select_reg_type("普通挂号")
    obj.select_doctor("华佗")
    obj.click_submit_btn()
