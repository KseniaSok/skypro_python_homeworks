from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#Откройте страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#Пять раз кликните на кнопку Add Element
for x in range(1, 6):
    click_on_button = driver.find_element(By.CSS_SELECTOR, ("[onclick='addElement()']")).click()
#Соберите со страницы список кнопок Delete
    delete_button = driver.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")
#Выведите на экран размер списка
print(f"Выведите на экран размер списка:{len(delete_button)}")