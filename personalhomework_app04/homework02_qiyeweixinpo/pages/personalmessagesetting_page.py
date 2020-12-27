
# 个人信息设置页面
from appium.webdriver.common.mobileby import MobileBy

from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage
from personalhomework_app04.homework02_qiyeweixinpo.pages.personalmessagedisplay_page import PersonalMessageDisplayPage


class PersonalMessageSettingPage(BasePage):
    def click_bjcy_button(self):
        # 点击编辑成员
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return PersonalMessageDisplayPage(self.driver)
