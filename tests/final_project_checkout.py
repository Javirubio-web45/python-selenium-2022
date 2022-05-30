from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.checkout_page import CheckoutPage


class TestCheckout:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test_add_and_remove_product(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.chose_canon_camera()
        checkout_page.add_to_cart("Blue")
        assert checkout_page.get_cart_total() == "1 item(s) - $98.00"
        checkout_page.remove_product()
        assert checkout_page.is_cart_empty() == "Your shopping cart is empty!"

    def test_checkout_structure(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.add_to_cart_iphone()
        checkout_page.move_to_checkout()
        assert checkout_page.is_checkout_header_visible()
        assert checkout_page.is_accordion_steps_visible()


    def teardown_method(self):
        if self.driver:
            self.driver.quit()