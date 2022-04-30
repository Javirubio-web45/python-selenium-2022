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

# TODO - Mejorar Xpaths

# Abrir pagina
driver.get(url)
driver.maximize_window()
time.sleep(3)
search: WebElement = driver.find_element(By.XPATH, '//header/div[1]/div[1]/div[2]/div[1]/input[1]')
assert search.is_displayed(), "Input no es visible"

search_btn : WebElement = driver.find_element(By.XPATH, '//header/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]')
assert search_btn.is_displayed(), "boton no es visible"

input = "iphone"
search.clear()
search.send_keys(input)
search_btn.click()

image : WebElement = driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/img[1]')
assert image.is_displayed(), "Imagen no es visible"
time.sleep(2)

image.click()
time.sleep(2)

# Cerrar navegador
driver.quit()