from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestDownload:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_medium())

    def test_no_products(self):
        """Ejercicio 13"""
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        # search bar
        input_bar: WebElement = self.driver.find_element(By.CLASS_NAME, 'input-lg')
        self.wait.until(EC.element_to_be_clickable(input_bar))
        input_bar.send_keys("Display")

        # search button
        search_btn: WebElement = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        self.wait.until(EC.element_to_be_clickable(search_btn))
        search_btn.click()

        # message no products found
        message_locator = (By.XPATH, "//div[@id='content']/p[2]")
        no_product_message = "There is no product that matches the search criteria."
        assert self.wait.until(EC.text_to_be_present_in_element(message_locator, no_product_message))

        # check box
        box_description: WebElement = self.driver.find_element(By.ID, "description")
        self.wait.until(EC.element_to_be_clickable(box_description))
        box_description.click()

        #search button
        search_btn_display: WebElement = self.driver.find_element(By.ID, "button-search")
        self.wait.until(EC.element_to_be_clickable(search_btn_display))
        search_btn_display.click()

        #items locators
        samsung_locator = (By.XPATH, "//a[contains(text(),'Apple Cinema 30')]")
        nano_locator = (By.XPATH, "//a[contains(text(),'iPod Nano')]")
        touch_locator = (By.XPATH, "//a[contains(text(),'iPod Touch')]")
        macbook_locator = (By.XPATH, "//a[contains(text(),'MacBook Pro')]")

        #items assertions
        assert self.wait.until(EC.visibility_of_element_located(samsung_locator)), "El elemento samsung no esta disponible"
        assert self.wait.until(EC.visibility_of_element_located(nano_locator)), "El elemento nano no esta disponible"
        assert self.wait.until(EC.visibility_of_element_located(touch_locator)), "El elemento touch no esta disponible"
        assert self.wait.until(EC.visibility_of_element_located(macbook_locator)), "El elemento macbook no esta disponible"

    def test_add_to_cart(self):
        """Ejercicio 14"""
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        #menu MAC
        desktop_btn_locator = (By.XPATH, "//ul[@class='nav navbar-nav']/li[1]/a")
        desktop_btn: WebElement = self.wait.until(EC.element_to_be_clickable(desktop_btn_locator))
        desktop_btn.click()

        #open product
        mac_option_locator = (By.XPATH, "//a[contains(text(),'Mac')]")
        mac_option: WebElement = self.wait.until(EC.element_to_be_clickable(mac_option_locator))
        mac_option.click()

        #add iMAC
        imac_locator = (By.XPATH, "//a[contains(text(),'iMac')]")
        assert self.wait.until(EC.visibility_of_element_located(imac_locator)), "El elemento imac no esta disponible"
        imac_btn: WebElement = self.driver.find_element(By.XPATH, "//a[contains(text(),'iMac')]")
        imac_btn.click()

        #cart button
        add_btn_locator = (By.ID, "button-cart")
        add_btn: WebElement = self.wait.until(EC.element_to_be_clickable(add_btn_locator))
        add_btn.click()

        cart_btn_locator = (By.ID, "cart-total")
        assert self.wait.until(EC.text_to_be_present_in_element(cart_btn_locator, "1 item(s) - $122.00")), "item was not added"


    def test_currency(self):
        """Ejercicio 15"""
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        #symbol currency
        currency_symbol_locator = (By.TAG_NAME, "strong")
        assert self.wait.until(EC.text_to_be_present_in_element(currency_symbol_locator, "$"), "No esta el simbolo")

        #search bar
        input_bar_locator = (By.CLASS_NAME, 'input-lg')
        input_bar: WebElement = self.wait.until(EC.element_to_be_clickable(input_bar_locator))
        input_bar.send_keys("Samsung")

        #seacrh button
        search_btn_locator = (By.XPATH, "//button[@class='btn btn-default btn-lg']")
        search_btn: WebElement = self.wait.until(EC.element_to_be_clickable(search_btn_locator))
        search_btn.click()

        #samsung item
        samsung_model_locator = (By.XPATH, "//a[contains(text(),'Samsung SyncMaster 941BW')]")
        samsung_model: WebElement = self.wait.until(EC.element_to_be_clickable(samsung_model_locator))
        samsung_model.click()

        #Dollar price
        price_dollar_locator: WebElement = self.driver.find_element(By.XPATH, "//div[@id='content']/div/div[2]/ul[2]/li[1]/h2")
        price_dollar = price_dollar_locator.text
        dollar = float(price_dollar[1:])

        #Currency button
        currency_btn_locator = (By.XPATH, "//button[@class='btn btn-link dropdown-toggle']")
        currency_btn: WebElement = self.wait.until(EC.element_to_be_clickable(currency_btn_locator))
        currency_btn.click()

        #Euro currency
        euro_btn_locator = (By.NAME, "EUR")
        euro_btn: WebElement = self.wait.until(EC.element_to_be_clickable(euro_btn_locator))
        euro_btn.click()

        #Euro price
        price_euro_locator: WebElement = self.driver.find_element(By.XPATH, "//div[@id='content']/div/div[2]/ul[2]/li[1]/h2")
        price_euro = price_euro_locator.text
        euro = float(price_euro[:-1])

        assert euro < dollar, "Euro no es menor a dollar"






    def teardown_method(self):
        if self.driver:
            self.driver.quit()