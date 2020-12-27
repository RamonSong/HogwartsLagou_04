from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from personalhomework_web03.homework02_lianxirenpo.pages.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver


    def add_qiyecy(self, name, idnumber, phonenumber):
        # name = "zzz0"
        # idnumber = "zzz0-0001"
        # phonenumber = "13930102030"
        self.find(By.ID, 'username').send_keys(name)
        # 传入账号
        self.find(By.XPATH, '//*[@placeholder="成员唯一标识，设定以后不支持修改"]').send_keys(idnumber)
        # 传入电话
        self.find(By.XPATH, '//*[@placeholder="成员通过验证该手机后可加入企业"]').send_keys(phonenumber)
        # 点击保存
        self.find(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()

        return True

    def getchengyuan(self):
        elements = self.find(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        titles= [element.get_attribute('title') for element in elements]
        return titles