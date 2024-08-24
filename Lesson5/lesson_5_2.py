from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
#Откройте страницу http://uitestingplayground.com/dynamicid
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
#Кликните на синюю кнопку.
#Запустите скрипт три раза подряд.
for i in range(3):
    bluebutton = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")