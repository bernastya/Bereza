from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

search_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
search_field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button#updatingButton").click()

text = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")

print(text.text)

driver.quit()
