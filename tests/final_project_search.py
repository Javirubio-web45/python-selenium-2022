from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.search_page import SearchPage


class TestSearch:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test_search_apple_products(self):
        search_page = SearchPage(self.driver)
        search_page.search_a_product("Apple")
        search_page.advanced_search()
        search_page.select_mac_pro()
        assert search_page.get_brand_name() == "Apple", "Brand name should be 'Apple'"
        search_page.select_brand_apple()
        assert search_page.is_brand_appel_visible()

    def test_advanced_search(self):
        search_page = SearchPage(self.driver)
        search_page.search_a_product("Camera")
        search_page.advanced_search("Cameras")
        assert search_page.get_name_result() == "Nikon D300", "Result should be 'Nikkon D300'"

    def test_invalid_search(self):
        search_page = SearchPage(self.driver)
        search_page.search_a_product("Invalid")
        assert search_page.get_no_product_message() == "There is no product that matches the search criteria.", "Message is not the expected"


    def teardown_method(self):
        if self.driver:
            self.driver.quit()