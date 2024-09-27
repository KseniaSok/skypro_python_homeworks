from selenium.webdriver.common.by import By
from Lesson7.URL import three_url

class ShopMainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(three_url)
    
    def registration(self):
        self._name = (By.ID, 'user-name')
        self._pass = (By.ID, 'password')
        self._log_button = (By.ID, 'login-button')
        self.browser.find_element(*self._name).send_keys('standard_user')
        self.browser.find_element(*self._pass).send_keys('secret_sauce')
        self.browser.find_element(*self._log_button).click()
    
    def buy(self):
        self.SauceLabsBackpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.SauceLabsBoltTShirt = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        self.SauceLabsOnesie = (By.ID, 'add-to-cart-sauce-labs-onesie')

    def click(self):
        self.browser.find_element(*self.SauceLabsBackpack).click()
        self.browser.find_element(*self.SauceLabsBoltTShirt).click()
        self.browser.find_element(*self.SauceLabsOnesie).click()

    def container(self):
        self.Container = (By.ID, 'shopping_cart_container')
        self.browser.find_element(*self.Container).click()