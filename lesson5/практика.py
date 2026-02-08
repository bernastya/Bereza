#from time import sleep
#from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get ("https://www.example.com/")

#print(f'Заголовок страницы: {driver.title}')

#driver.quit()


#from time import sleep
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()
#driver.get ("https://www.python.org/")

#driver.find_element(By.LINK_TEXT, "Donate").click()

#driver.quit()


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#открыть сайт 
driver.get("https://www.google.com/")

  # Найти строку поиска и ввести "Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")

    # Нажать Enter для выполнения поиска
search_box.send_keys(Keys.RETURN)

driver.quit()

