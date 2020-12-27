
# 个人信息详情展示页
from appium.webdriver.common.mobileby import MobileBy
import time
from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage


class PersonalMessageDisplayPage(BasePage):
    def click_deletechengyuan_button(self):
        name = "AAA"
        # 点击删除成员
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # 点击确定
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        time.sleep(2)
        ele2 = self.finds(MobileBy.XPATH,
                                         f"//*[contains(@class, 'android.widget.TextView') and contains(@text, '{name}')]")
        afternum = len(ele2)
        print(afternum)
        from personalhomework_app04.homework02_qiyeweixinpo.pages.search_page import SearchPage
        return SearchPage(self.driver)