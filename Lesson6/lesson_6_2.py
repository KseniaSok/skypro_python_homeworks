from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get ("http://uitestingplayground.com/textinput")
driver.implicitly_wait(20)

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName.form-control")
element.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton.btn.btn-primary")
button.click()

txt = button.text
print(txt)

driver.quit()