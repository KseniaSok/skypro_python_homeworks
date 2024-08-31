from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys('Иван')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="last-name"]').send_keys('Петров')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys('Ленина, 55-3')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys('Москва')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys('Россия')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys('test@skypro.com')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys('+7985899998787')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys('QA')
driver.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys('SkyPro')
sleep(5)
driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3').click()
sleep(5)
WebDriverWait(driver, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))  
assert 'danger' in driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#first-name').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#last-name').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#address').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#city').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#coubtry').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#e-mail').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#phone').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#job-position').get_attribute("class")
assert 'success' in driver.find_element(By.CSS_SELECTOR, '#company').get_attribute("class")
sleep(5)
driver.quit()