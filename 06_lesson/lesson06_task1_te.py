from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def button(driver):

    driver.get("http://uitestingplayground.com/ajax")
   
    driver.find_element(By.CSS_SELECTOR, "#ajaxButton").clicdef test_...k()
    driver.implicitly_wait(20)
    text = driver.find_element(By.CSS_SELECTOR, "p.bg-success")
    print(text.text)
    driver.quit()


button()