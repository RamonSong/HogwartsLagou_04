import shelve

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class TestAdds:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(('name, idnumber, phonenumber'), yaml.safe_load(open("./data01.yml"))['Testdata'])
    def test_addlianxiren(self, name, idnumber, phonenumber):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'TgJdKLzS9ReE9Zt7rbLhtjUDxd8slKLsTuc8eHIqVoBXVn5eaUzfTuHAyuBHoS5PxwSEWSOUB6aoQuttu7rVOMYlmMTKTdac5bGN3o1c9-klb6xCeTODhKVpAQISow5VJmTdw2Y4DexuD98iraIp9mOSNcOrAWDMHf5SGcDvsLQlaJyQQ0PbROwEovsuFwqfB7SVHNQi75G7oukHshTG-VZ_htFq8PnWh6F3OFmZ50IXzE1R2P_5j_S88tEHVcsIKbh0AhEtcMkgPvSyl0qsVg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'zNQh0Z_s46ABnw4DwqdavyH-Yrb5_6xd2PUpjQf-VPKrJQTISPaE3iZgU3ptBs1D'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3069698'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853349883344'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853349883344'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325040202148'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '24820931753041740'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1607277211, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '2uja6f7'},
            {'domain': '.qq.com', 'expiry': 1607356253, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1524495547.1607245700'},
            {'domain': '.qq.com', 'expiry': 1670341853, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.174200240.1607245700'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1638781675, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '0f0a9c03aa1105956543e05889042cb20f2c819de523328b5fb62ecba77fbb4e'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1638781680, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1607245681'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'EqZsB/ETFH'},
            {'domain': '.qq.com', 'expiry': 1609676554, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '1229069593'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1609862608, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '6427226112'}]
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # cookies = self.driver.get_cookies()
        # print(cookies)

        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        # 点击添加成员
        # self.driver.find_element(By.XPATH, '//*[@class="index_service_cnt js_service_list"]//a[@class="index_service_cnt_itemWrap"][1]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        # # self.driver.find_element(By.LINK_TEXT, '添加成员').click()
        # 传入名字
        self.driver.find_element(By.ID, 'username').send_keys(f'{name}')
        # 传入账号
        self.driver.find_element(By.XPATH, '//*[@placeholder="成员唯一标识，设定以后不支持修改"]').send_keys(f'{idnumber}')
        # 传入电话
        self.driver.find_element(By.XPATH, '//*[@placeholder="成员通过验证该手机后可加入企业"]').send_keys(f'{phonenumber}')
        # 点击保存
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        # 获取保存成功的文字
        aa = self.driver.find_element(By.XPATH, '/html/body/div[3]').text
        # 断言是否保存成功
        assert aa == '保存成功'
