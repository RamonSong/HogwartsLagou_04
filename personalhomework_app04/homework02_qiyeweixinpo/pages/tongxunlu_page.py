
#通讯录页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from personalhomework_app04.homework02_qiyeweixinpo.pages.addlianxiren_page import AddLianXiRenPage
from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage
from personalhomework_app04.homework02_qiyeweixinpo.pages.search_page import SearchPage


class TongXunLuPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def click_add_chengyuan(self):
        # 滚动查找添加成员按钮并点击
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        return AddLianXiRenPage(self.driver)



    def click_search_button(self):
        # 点击搜索按钮
        self.find(MobileBy.ID, 'com.tencent.wework:id/hvn').click()
        return SearchPage(self.driver)





