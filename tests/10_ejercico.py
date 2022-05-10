from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)

btn_locator = (By.ID, "autoclosable-btn-success")
btn_msg: WebElement = wait.until(EC.element_to_be_clickable(btn_locator))
#assert btn_asm.is_enabled(), "El boton no esta disponible"
btn_msg.click()

alert_locator = (By.CLASS_NAME, "alert-autocloseable-success")

wait.until(EC.visibility_of_element_located(alert_locator))

assert wait.until(EC.invisibility_of_element_located(alert_locator)), "El elemento aun se ve"

driver.quit()

