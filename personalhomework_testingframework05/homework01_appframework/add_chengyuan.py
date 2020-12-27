import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


def load_data(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)

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


    @pytest.mark.parametrize(('name, gender, phonenumber'), load_data('./test_data.yml')['Data'])
    def test_addlianxiren(self, name, gender, phonenumber):
        for step in load_data('./test_data.yml')['Steps']:
            print(step)
            if 'find_element' in step:
                by = step.get("find_element")[0]
                locator = step.get("find_element")[1]
                current_situtation = self.driver.find_element(by, locator)


            if "click" in step:
                current_situtation.click()


            if "send_keys" in step:
                value = str(step.get("send_keys"))
                current_situtation.send_keys(value)


            if "text" in step:
                text01 = step.get("text")
                assert text01 == "添加成功"



        # name = "QQQ"
        # gender = '男'
        # phonenumber = '19912341099'
        # 点击通讯录
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # # 滚动查找添加成员按钮并点击
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        # # 点击手动输入添加
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # # 输入姓名
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(name)
        # #输入性别为男
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        # if gender =='男':
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # # 输入手机号
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/../android.widget.EditText").send_keys(phonenumber)
        # # 点击保存
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # result = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        # assert result == "添加成功"
