from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
#Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver.get("http://the-internet.herokuapp.com/entry_ad")
wait = WebDriverWait(driver, 10)
modal_window = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
#В модальном окне нажмите на кнопку Сlose
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer .close-button")))