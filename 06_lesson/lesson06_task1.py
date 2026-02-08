from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

driver.implicitly_wait(20)

text = driver.find_element(By.CSS_SELECTOR, "p.bg-success")

print(text.text)

driver.quit()
