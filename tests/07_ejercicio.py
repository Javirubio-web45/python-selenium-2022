from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)

locator = (By.ID, "at-cv-lightbox-close")
#locator = (By.ID, "at-cv-lightbox-content")
#locator = (By.LINK_TEXT, "No, thanks!'")
search_popup = wait.until(EC.visibility_of_element_located(locator))
assert search_popup.is_enabled(), "boton de cerrar del popup est habilitado"

search_popup.click()

driver.quit()