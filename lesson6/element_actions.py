from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService())

driver.get("https://ya.ru") #переход на сайт

element = driver.find_element(By.CSS_SELECTOR, "#text") #нашли элемент
element.send_keys("test skypro") #отправляем текст
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

#sleep(3)

#element.clear() #очищаем текстовое поле

sleep(5)

driver.quit()
