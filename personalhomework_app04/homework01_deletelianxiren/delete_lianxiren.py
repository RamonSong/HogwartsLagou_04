import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestQiYeWeiXin:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_addlianxiren(self):
        name = "AAA"
        gender = '男'
        phonenumber = '19912341090'
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找添加成员按钮并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(name)
        #输入性别为男
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        if gender =='男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # 输入手机号
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/../android.widget.EditText").send_keys(phonenumber)
        # 点击保存
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        result = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        assert result == "添加成功"




    def test_deletelianxiren(self):
        name = "AAA"
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # # 滚动查找成员AAA
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("AAA").instance(0));').click()
        # 点击搜索按钮
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hvn').click()
        # 输入需要查找的成员名字
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        time.sleep(2)
        # 获取查询结果数量
        ele1 = self.driver.find_elements(MobileBy.XPATH, "//*[contains(@class, 'android.widget.TextView') and contains(@text, 'AAA')]")
        beforenum = len(ele1)
        print(beforenum)
        # 点击查找到的联系人
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@class, 'android.widget.TextView') and contains(@text, 'AAA')]").click()
        # 点击右上角更多按钮
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hvd').click()
        # 点击编辑成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # 点击删除成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # 点击确定
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        time.sleep(2)
        ele2 = self.driver.find_elements(MobileBy.XPATH, "//*[contains(@class, 'android.widget.TextView') and contains(@text, 'AAA')]")
        afternum = len(ele2)
        assert afternum == beforenum - 1



