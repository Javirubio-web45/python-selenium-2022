from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.login_page import LoginPage


class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get("https://laboratorio.qaminds.com/index.php?route=account/login")

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login('asdsgjj@mail.com', 'asdsdf123')
        assert login_page.is_login_warn_displayed()

    def test_forgotten_password(self):
        pass

    def test_continue_as_new_customer(self):
        pass

    def test_select_menu(self):
        pass

    def test_cart(self):
        pass


    def teardown_method(self):
        if self.driver:
            self.driver.quit()