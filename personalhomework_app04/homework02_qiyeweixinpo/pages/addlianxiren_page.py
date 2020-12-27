
#添加成员页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage
from personalhomework_app04.homework02_qiyeweixinpo.pages.editmessage_page import EditMessagePage


class AddLianXiRenPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    def click_handadds(self):
        # 点击手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditMessagePage(self.driver)


    def get_vertify_toast(self):
        # result = self.find(MobileBy.XPATH, "//*[@text='添加成功']").text
        result = self.get_toast()
        return result