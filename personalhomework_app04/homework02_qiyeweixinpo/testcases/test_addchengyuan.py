from personalhomework_app04.homework02_qiyeweixinpo.pages.app import App


class TestQiYeWeiXin:
    def setup(self):
        self.app = App()
        self.main = self.app.start().go_to_main()
        pass


    def teardown(self):
        self.app.stop()


    def test_adds(self):
        name = "zzzz"
        gender = '男'
        phonenumber = '19912341099'

        result = self.main.go_to_tongxunlu().click_add_chengyuan().\
            click_handadds().edit_message(name, gender, phonenumber).get_vertify_toast()
        assert "添加成功" == result