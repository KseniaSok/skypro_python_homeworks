from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Alex')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Fox')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('123456')
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total_label = driver.find_element(By.CSS_SELECTOR, '[data-test=total-label]').text
    assert total_label == ('Total: $58.29')

    driver.quit()