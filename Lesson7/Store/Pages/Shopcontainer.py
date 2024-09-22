from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ShopContainer:
    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        self.check = (By.ID, 'checkout')
        self.browser.find_element(*self.check).click()

    def info(self):
        self.first_name = (By.ID, 'first-name')
        self.browser.find_element(*self.first_name).send_keys('Alex')
        self.last_name = (By.ID, 'last-name')
        self.browser.find_element(*self.last_name).send_keys('Fox')
        self.postal_code = (By.ID, 'postal-code')
        self.browser.find_element(*self.postal_code).send_keys('123456')
        self.continue_button = (By.ID, 'continue')
        self.browser.find_element(*self.continue_button).click()

    def price(self):
        WebDriverWait(self.browser, 10, 0.1).until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, '[data-test=total-label]')).text
        total_label = self.browser.find_element(By.CSS_SELECTOR, '.summary_total_label')
        total = total_label.text.strip().replace('Total: $', '')
        return total