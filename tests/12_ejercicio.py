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

    def test_download_button_1(self):
        """Ejercicio 8"""
        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

        download_btn: WebElement = self.driver.find_element(By.ID, 'downloadButton')
        assert download_btn.is_enabled(), "Boton de descarga no esta disponible"
        download_btn.click()

        locator = (By.XPATH, "//button[contains(text(),'Close')]")
        close_btn = self.wait.until(EC.visibility_of_element_located(locator))
        assert close_btn.is_enabled(), "Boton close no esta disponible"

        complete_msg: WebElement = self.driver.find_element(By.XPATH, "//div[contains(text(),'Complete!')]")
        assert complete_msg.text == "Complete!", "No se encontro el mensaje con la frase 'Complete!'"

        close_btn.click()

    def test_download_button_2(self):
        """Ejercicio 9"""
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")

        locator = (By.ID, "cricle-btn")
        download_btn_ready = self.wait.until(EC.visibility_of_element_located(locator))
        assert download_btn_ready.is_enabled(), "El boton no esta disponible"
        download_btn: WebElement = self.driver.find_element(By.ID, "cricle-btn")

        download_btn.click()

        locator_msg = (By.CLASS_NAME, "percenttext")
        #percent_indicator = self.wait.until(EC.visibility_of_element_located(locator_msg))
        #assert percent_indicator.is_enabled(), "No se descargo al 100%"

        assert self.wait.until(EC.visibility_of_element_located(locator_msg)), "No se descargo al 100%"

    def test_auto_closable_msg(self):
        """Ejercicio 10"""
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html")

        btn_locator = (By.ID, "autoclosable-btn-success")
        btn_msg: WebElement = self.wait.until(EC.element_to_be_clickable(btn_locator))
        # assert btn_asm.is_enabled(), "El boton no esta disponible"
        btn_msg.click()

        alert_locator = (By.CLASS_NAME, "alert-autocloseable-success")

        self.wait.until(EC.visibility_of_element_located(alert_locator))

        assert self.wait.until(EC.invisibility_of_element_located(alert_locator)), "El elemento aun se ve"

    def teardown_method(self):
        if self.driver:
            self.driver.quit()