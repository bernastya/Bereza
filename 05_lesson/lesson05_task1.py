from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
driver.get("http://uitestingplayground.com/classattr/")

sleep(5)

driver.find_element(By.CLASS_NAME, "btn.class3.btn-primary.btn-test").click()

sleep(10)

#задание1