from personalhomework_web03.homework02_lianxirenpo.pages.main_page import MainPage


class TestAdd:
    def setup(self):
        self.main = MainPage()


    def test_add_cy(self):
        name = "zzz0"
        idnumber = "zzz0-0001"
        phonenumber = "13930102030"
        result1 = self.main.click_add_chengyuan()
        result1.add_qiyecy(name, idnumber, phonenumber)
        aa = result1.getchengyuan()
        assert name in aa