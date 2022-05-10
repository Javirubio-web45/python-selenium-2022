from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)

locator = (By.ID, "cricle-btn")
download_btn_ready = wait.until(EC.visibility_of_element_located(locator))
assert download_btn_ready.is_enabled(), "El boton no esta disponible"
download_btn: WebElement = driver.find_element(By.ID, "cricle-btn")

download_btn.click()

locator_msg = (By.CLASS_NAME, "percenttext")
#percent_indicator = wait.until(EC.visibility_of_element_located(locator_msg))
#assert percent_indicator.is_enabled(), "No se descargo al 100%"

assert wait.until(EC.visibility_of_element_located(locator_msg)), "No se descargo al 100%"

driver.quit()
