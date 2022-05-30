from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.login_page import LoginPage



class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.move_to_login()
        login_page.login('asdsgjj@mail.com', 'asdsdf123')
        assert login_page.is_login_warn_displayed()

    def test_forgotten_password(self):
        login_page = LoginPage(self.driver)
        login_page.move_to_login()
        login_page.move_to_forgotten_password()
        assert login_page.is_forgot_password_header_visible(), "'Forgot Your Password?', should be visible"
        assert login_page.is_email_address_legend_visible(), "'Your E-Mail Address' should be visible"
        assert login_page.is_email_address_label_visible(), "'E-Mail Address', should be visible"
        login_page.return_to_login()
        assert login_page.is_returning_customer_visible(), "You should be in the login section"

    def test_access_to_register(self):
        login_page = LoginPage(self.driver)
        login_page.move_to_login()
        assert login_page.is_new_customer_header_visible(), "'New Customer' header should be visible"
        assert login_page.is_register_account_text_visible(), "'Register Account' text should be visible"
        login_page.move_to_register_account()
        assert login_page.is_register_account_header_visible(), "'Register Account' header should be visible"

    def teardown_method(self):
        if self.driver:
            self.driver.quit()