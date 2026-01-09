from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
     service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://www.firefox.com/")
driver.get("https://the-internet.herokuapp.com/inputs")

sleep(5)

search_field = driver.find_element(By.CSS_SELECTOR, 'input')
search_field.send_keys("Sky")

sleep(5)

search_field.clear()
search_field.send_keys("Pro")

sleep(5)

driver.quit()

#задание3

