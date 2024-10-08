from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 40, 0.1)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p#text.lead"), "Done!"))
waiter.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

attribute = driver.find_element(By.ID, "award")
attribute.get_attribute("src")
print(attribute.get_attribute("src"))

driver.quit()