from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://www.firefox.com/")
driver.get("https://the-internet.herokuapp.com/login")

sleep(5)

search_field = driver.find_element(By.NAME, 'username')
search_field.send_keys("tomsmith")

sleep(3)

search_field = driver.find_element(By.NAME, 'password')
search_field.send_keys("SuperSecretPassword!")

sleep(3)

driver.find_element(By.TAG_NAME, 'i').click()

text = driver.find_element(By.CSS_SELECTOR, "div#flash.flash.success")

print(text.text)

sleep(3)

driver.quit()

#задание 4