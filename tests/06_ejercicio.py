import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Init Browsers
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'
url = "https://demoqa.com/select-menu"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Web Page
driver.get(url)

# Test Logic
time.sleep(2)
cars = driver.find_element(By.ID, "cars")
assert cars.is_displayed(), "Cars is not visible"
#colors_dropdown = Select(colors)
cars_dropdown = Select(cars)
cars_dropdown.select_by_visible_text("Volvo")
#selected_option: WebElement = cars_dropdown.first_selected_option
#assert selected_option.text == "Volvo", "no se selecciono volvo"

cars_dropdown.select_by_visible_text("Audi")
#selected_option: WebElement = cars_dropdown.first_selected_option
#assert selected_option.text == "Audi", "no se selecciono audi"
selected_option: list = [item.text for item in cars_dropdown.all_selected_options]
assert "Volvo" in selected_option, "Volvo no fue selccionado"
assert "Audi" in selected_option, "Audi mno fue selccionado"
time.sleep(2)

driver.quit()



