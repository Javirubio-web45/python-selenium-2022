from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)

download_btn: WebElement = driver.find_element(By.ID, 'downloadButton')
assert download_btn.is_enabled(), "Boton de descarga no esta disponible"
download_btn.click()

locator = (By.XPATH, "//button[contains(text(),'Close')]")
close_btn = wait.until(EC.visibility_of_element_located(locator))
assert close_btn.is_enabled(), "Boton close no esta disponible"

complete_msg: WebElement = driver.find_element(By.XPATH, "//div[contains(text(),'Complete!')]")
assert complete_msg.text == "Complete!", "No se encontro el mensaje con la frase 'Complete!'"

close_btn.click()

driver.quit()
