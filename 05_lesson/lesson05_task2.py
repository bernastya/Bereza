from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
driver.get("http://uitestingplayground.com/dynamicid/")

sleep(10)

driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), \
' btn-primary ')]").click()

sleep(10)

#задание 2