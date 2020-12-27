
#app的基本操作，如启动、关闭、进入主页等
from appium import webdriver

from personalhomework_app04.homework02_qiyeweixinpo.pages.base_page import BasePage
from personalhomework_app04.homework02_qiyeweixinpo.pages.main_page import MainPage


class App(BasePage):

    def start(self):
        # 通过判断driver是否为空来决定是否复用APP，如果driver为None，则进行初始化启动APP，如果不为None则直接启动APP
        if self.driver == None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = '.launch.LaunchSplashActivity'
            caps['noReset'] = 'True'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(5)
        else:
            # 启动APP，启动的是desiredcaps里面的activity
            self.driver.launch_app()
        return self


    def restart(self):
        pass


    def stop(self):
        self.driver.quit()



    def go_to_main(self):
        return MainPage(self.driver)