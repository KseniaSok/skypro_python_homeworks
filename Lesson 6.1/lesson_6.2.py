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
driver.implicitly_wait(60)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.find_element(By.CSS_SELECTOR, '#delay').clear()
sleep(5)
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
sleep(5)
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()
sleep(50)
waiter = WebDriverWait(driver, 60, 1)
#checkout_summary_container > div > div.summary_info > div.summary_total_labeldriver.quit()