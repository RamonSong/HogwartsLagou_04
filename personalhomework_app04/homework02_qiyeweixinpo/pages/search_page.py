
# 搜索页面
import time

from appium.webdriver.common.mobileby import MobileBy

from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage
from personalhomework_app04.homework02_qiyeweixinpo.pages.click_findscy_page import ClickFindsCyPage


class SearchPage(BasePage):
    def shuru_and_autosearch(self, name):

        # 输入需要查找的成员名字并等待
        self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        time.sleep(2)
        # 获取查询结果数量
        ele1 = self.finds(MobileBy.XPATH,
                                         f"//*[contains(@class, 'android.widget.TextView') and contains(@text, '{name}')]")
        beforenum = len(ele1)
        print(beforenum)

        # 点击查找到的联系人
        self.find(MobileBy.XPATH,
                                 f"//*[contains(@class, 'android.widget.TextView') and contains(@text, '{name}')]").click()

        return ClickFindsCyPage(self.driver)


    def additionalshuru(self, name):

        # 输入需要查找的成员名字
        contents = self.find(MobileBy.XPATH, "//*[@text='搜索']").text
        if contents == None:
            self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
            time.sleep(2)
        elif contents != None:
            time.sleep(2)
    

