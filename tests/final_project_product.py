from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.product_page import ProductPage


class TestProduct:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test_apple_products(self):
        product_page = ProductPage(self.driver)
        product_page._move_to_tablets()
        product_page._select_galaxy_tab()
        assert product_page.get_name() == 'Samsung Galaxy Tab 10.1'
        assert product_page.get_price() == '$241.99'
        assert product_page.get_ex_tax() == '$199.99'
        assert product_page.get_product_code() == 'SAM1'
        assert product_page.get_reward_points() == '1000'
        assert product_page.get_availability() == 'Pre-Order'

    def test_send_a_review(self):
        product_page = ProductPage(self.driver)
        product_page._move_to_monitors()
        product_page._select_samsung_syncmaster()
        product_page._send_a_review("Juan Lopez", "Is a good product, is amazing!!!")
        assert product_page._get_alert_success() == "Thank you for your review. It has been submitted to the webmaster for approval.", "Alert success message is not the expected"


    def teardown_method(self):
        if self.driver:
            self.driver.quit()