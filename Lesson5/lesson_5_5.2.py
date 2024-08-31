from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
#Откройте страницу http://the-internet.herokuapp.com/inputs
driver.get("http://the-internet.herokuapp.com/inputs")
#Введите в поле текст 1000
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
#Очистите это поле (метод clear)
input_field.clear()
#Введите в это же поле текст 999
input_field.send_keys("999")
driver.quit()