from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
#Откройте страницу http://uitestingplayground.com/classattr.
#Кликните на синюю кнопку.
#Запустите скрипт три раза подряд. 
for i in range(3):
    driver.get("http://uitestingplayground.com/classattr")
    bluebutton = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    alert = driver.switch_to.alert
    alert.accept()
print(f"нажали на кнопку {i} раз(а)")
driver.quit()