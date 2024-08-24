from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
#Откройте страницу http://the-internet.herokuapp.com/login
driver.get("http://the-internet.herokuapp.com/login")
#В поле username введите значение tomsmith
login_field = "#login-field"
login_input = driver.find_element(By.CSS_SELECTOR, login_field)
login_input.send_keys("tomsmith")
#В поле password введите значение SuperSecretPassword!
password_field = "#password-field"
password_input = driver.find_element(By.CSS_SELECTOR, password_field)
password_input.send_keys("SuperSecretPassword!")
#Нажмите кнопку Login
button_login = driver.find_element(By.CSS_SELECTOR, "button[class='fa fa-2x fa-sign-in']")