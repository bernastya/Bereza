from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 30)

waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#award")))

src = driver.find_element(By.CSS_SELECTOR, "#award").get_dom_attribute("src")

print(src)
