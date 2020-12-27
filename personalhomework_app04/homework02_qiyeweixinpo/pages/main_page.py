
#主页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage
from personalhomework_app04.homework02_qiyeweixinpo.pages.tongxunlu_page import TongXunLuPage


class MainPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    def go_to_tongxunlu(self):
        # 点击通讯录
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return TongXunLuPage(self.driver)



