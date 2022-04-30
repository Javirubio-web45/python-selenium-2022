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
dropdown: WebElement = driver.find_element(By.LINK_TEXT, 'My Account')
assert dropdown.is_displayed(), "dropdown no es visible"
dropdown.click()

login_btn: WebElement = driver.find_element(By.XPATH, '//a[contains(text(),"Login")]')
assert login_btn.is_displayed(), "Login no es visible"
login_btn.click()
time.sleep(2)

email_address: WebElement = driver.find_element(By.ID, 'input-email')
assert email_address.is_displayed(), "input email no es visible"
email_address.send_keys("asdfg")

password: WebElement = driver.find_element(By.ID, 'input-password')
assert password.is_displayed(), "password input no es visible"
password.send_keys("123456")

login_btn_user : WebElement = driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/input[1]")
assert login_btn_user.is_displayed(), "login boton logear usuario no es visible"
login_btn_user.click()

warning : WebElement = driver.find_element(By.XPATH, '//*[@id="account-login"]/div[1]')
assert warning.is_displayed(), "warning no es visible"
assert warning.text == " Warning: No match for E-Mail Address and/or Password.", "No es el mensaje esperado"

time.sleep(2)


# Cerrar navegador
driver.quit()