from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
#Откройте страницу http://the-internet.herokuapp.com/login
driver.get("http://the-internet.herokuapp.com/login")
#В поле username введите значение tomsmith
input_username = driver.find_element(By.ID, "username").send_keys("tomsmith")
#В поле password введите значение SuperSecretPassword!
input_password = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
#Нажмите кнопку Login
button_login = driver.find_element(By.TAG_NAME, "button").click()
driver.quit()