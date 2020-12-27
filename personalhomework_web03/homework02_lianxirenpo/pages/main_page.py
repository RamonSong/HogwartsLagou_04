from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from personalhomework_web03.homework02_lianxirenpo.pages.addmember_page import AddMemberPage
from personalhomework_web03.homework02_lianxirenpo.pages.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"


    def click_add_chengyuan(self):
        self.find(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMemberPage(self.driver)


