

# 查找到的要删除的目标成员页面
from appium.webdriver.common.mobileby import MobileBy

from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage
from personalhomework_app04.homework02_qiyeweixinpo.pages.personalmessagesetting_page import PersonalMessageSettingPage


class ClickFindsCyPage(BasePage):
    def click_more_operation(self):
        # 点击右上角更多按钮
        self.find(MobileBy.ID, 'com.tencent.wework:id/hvd').click()
        return PersonalMessageSettingPage(self.driver)