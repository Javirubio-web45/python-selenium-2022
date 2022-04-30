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
time.sleep(2)

tablets_btn: WebElement = driver.find_element(By.XPATH, '//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[4]/a[1]')
assert tablets_btn.is_displayed(), "Boton tablets no es visible"
tablets_btn.click()
time.sleep(2)

titulo_samsung : WebElement = driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/h4[1]/a[1]')
assert titulo_samsung.is_displayed(), "Samsung no es visible"
titulo_samsung.click()
time.sleep(2)

precio : WebElement = driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[1]/h2[1]')
assert precio.is_displayed(), "precio no es visible"
assert precio.text == "$241.99", "No es el mismo precio"

wish_list_btn : WebElement = driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/i[1]')
assert wish_list_btn.is_displayed(), "boton wish list no es visible"
wish_list_btn.click()
time.sleep(2)

add_cart : WebElement = driver.find_element(By.ID, 'button-cart')
assert add_cart.is_displayed(), "boton add to cart no es visible"
add_cart.click()

time.sleep(2)


# Cerrar navegador
driver.quit()