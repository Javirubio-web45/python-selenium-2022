import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Inicializar driver
chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://laboratorio.qaminds.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# TODO - Encontrar el XPath para el warning

# Abrir pagina
driver.get(url)
driver.maximize_window()
time.sleep(3)
navbar_laps_end_note: WebElement = driver.find_element(By.LINK_TEXT, 'Laptops & Notebooks')
assert navbar_laps_end_note.is_displayed(), "laptops y notebooks no es visible"
navbar_laps_end_note.click()

windows_btn: WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, 'Windows')
assert windows_btn.is_displayed(), "boton de windows no es visible"
windows_btn.click()
time.sleep(2)

message_windows: WebElement = driver.find_element(By.XPATH, "//p[contains(text(),'There are no products to list in this category.')]")
assert message_windows.is_displayed(), "mensaje de la ventana windows no es visible"

continue_btn: WebElement = driver.find_element(By.LINK_TEXT, 'Continue')
assert continue_btn.is_displayed(), "Boton de continue no es visible"
continue_btn.click()

slides_home : WebElement = driver.find_element(By.ID, "slideshow0")
assert slides_home.is_displayed(), "Slides de home no es visible"

time.sleep(2)


# Cerrar navegador
driver.quit()