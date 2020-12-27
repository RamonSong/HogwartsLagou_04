from personalhomework_app04.homework02_qiyeweixinpo.pages.app import App


class TestQiYeWX:
    def setup(self):
        self.app = App()
        self.main = self.app.start().go_to_main()
        pass


    def teardown(self):
        self.app.stop()


    def test_deletes(self):
        name = "AAA"
        result01 = self.main.go_to_tongxunlu().click_search_button().\
            shuru_and_autosearch(name).click_more_operation().\
            click_bjcy_button().click_deletechengyuan_button().additionalshuru(name)
        assert name in result01 == False
