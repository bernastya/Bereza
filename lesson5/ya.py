from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")
driver.get("https://vk.com/")
driver.set_window_size(640, 460)

sleep(10)

driver.save_screenshot("./ya.png")

# команды для активации виртуального окружения (.venv)

# .\.venv\Scripts\activate  (обрати внимание - .venv (с точкой ) название твоей папки. 
# Она иожет называться по-другому, тогда в команде с путем до файла activate также нужно поменять
# имя папки. То есть если папка будет называться "env", то команда активации будет выглядеть:
# .\env\Scripts\activate) Вызывать команду нуэно из корневой папки проекта. В твоем случае
# это папка Bereza