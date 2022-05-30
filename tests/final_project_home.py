from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage


class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test_back_to_home_page(self):
        home_page = HomePage(self.driver)
        home_page.select_login()
        assert home_page.is_logo_visible(), 'Login form should be visible'
        home_page.return_to_home_page()
        assert home_page.is_logo_visible(), 'Logo should be visible'


    def test_currency(self):
        home_page = HomePage(self.driver)
        home_page.set_currency("EUR")
        assert "€" == home_page.get_currency()
        home_page.set_currency("GBP")
        assert "£" == home_page.get_currency()
        home_page.set_currency("USD")
        assert "$" == home_page.get_currency()

    def test_carousels(self):
        home_page = HomePage(self.driver)
        assert home_page.is_top_carousel_visible(), 'top carousel should be visible'
        assert home_page.is_bottom_carousel_visible(), 'bottom carousel should be visible'


    def teardown_method(self):
        if self.driver:
            self.driver.quit()