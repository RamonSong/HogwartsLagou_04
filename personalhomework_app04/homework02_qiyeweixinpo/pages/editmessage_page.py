

#编辑成员页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage


class EditMessagePage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    def edit_message(self, name, gender, phonenumber):
        # 输入姓名
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(
            name)
        # 输入性别为男
        self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        if gender == '男':
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        # 输入手机号
        self.find(MobileBy.XPATH, "//*[contains(@text, '手机')]/../android.widget.EditText").send_keys(
            phonenumber)
        # 点击保存
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()


        from personalhomework_app04.homework02_qiyeweixinpo.pages.addlianxiren_page import AddLianXiRenPage
        return AddLianXiRenPage(self.driver)