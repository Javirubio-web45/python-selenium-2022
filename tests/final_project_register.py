from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.register_page import RegisterPage



class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test_register_account(self):
        register_page = RegisterPage(self.driver)
        register_page.move_to_register()
        assert register_page.is_register_account_header_visible(), "'Register Account' header should be present"
        assert register_page.is_personal_details_visible(), "'Your Personal Details' legend should be present"
        assert register_page.is_password_details_visible(), "'Your Password' legend should be present"

    def test_privacy_policy(self):
        register_page = RegisterPage(self.driver)
        register_page.move_to_register()
        assert register_page.get_warning_message() == 'Warning: You must agree to the Privacy Policy!', "'Warning: You must agree to the Privacy Policy!' should be visible"

    def teardown_method(self):
        if self.driver:
            self.driver.quit()