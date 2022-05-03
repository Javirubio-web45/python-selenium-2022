import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select

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
colors = driver.find_element(By.ID, "oldSelectMenu")
assert colors.is_displayed(), "Colors is not visible"
colors_dropdown = Select(colors)
colors_dropdown.select_by_visible_text("Green")

#old_style_select_menu : WebElement = driver.find_element(By.XPATH, "//select[@id='oldSelectMenu']")
#ossm_dropdown_list =  Select(old_style_select_menu)
#ossm_dropdown_list.select_by_visible_text("green")
#assert ossm_dropdown_list.text == "green", "no se selecciono green"
selected_option: WebElement = colors_dropdown.first_selected_option
assert selected_option.text == "Green", "no se selecciono green"
time.sleep(2)

driver.quit()