from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService())

#driver.get("https://ya.ru") #переход на сайт

#element = driver.find_element(By.CSS_SELECTOR, "#text") #нашли элемент
#element.send_keys("test skypro") #отправляем текст
#driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

#sleep(3)

#element.clear() #очищаем текстовое поле

#sleep(5)

#driver.quit()




#driver.get("http://uitestingplayground.com/visibility") #переход на сайт

#проверка видимости кнопки Opacity 0
#is_displayed = driver.find_element(
#By.CSS_SELECTOR, "#transparentButton").is_displayed() 

#print(is_displayed) #вывод статуса видимости Opacity 0

#driver.find_element(By.CSS_SELECTOR, "#hideButton").click() #нажатие на Hide
# Opacity 0 окажется скрытой
#sleep(2)

#еще раз проверим видимость Opacity 0:
#is_displayed = driver.find_element(
#By.CSS_SELECTOR, "#transparentButton").is_displayed()

#print(is_displayed) #еще раз выводим статус видимости Opacity 0

#sleep(2)

#driver.quit()


#driver.get("https://demoqa.com/radio-button")

#is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
#print(is_enabled)

#is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
#print(is_enabled)

#driver.quit()



#driver.get("https://the-internet.herokuapp.com/checkboxes")

#cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")

#is_selected = cb.is_selected()
#print(is_selected)

#sleep(3)

#cb.click()

#is_selected = cb.is_selected()
#print(is_selected)

#sleep(3)

#driver.quit()


#здесь по умолчанию идут команды для импорта драйвера, класса By и т.д.

#идем на страницу:
#driver.get("https://the-internet.herokuapp.com/checkboxes")

#записываем верхнюю html-ветку в переменную div
#div = driver.find_element(By.CSS_SELECTOR, "#page-footer")

#через div идем по ветке до элемента с тегом a
#a = div.find_element(By.CSS_SELECTOR, "a")

#запрашиваем ссылку из элемента с тегом a
#print(a.get_attribute("href"))

#driver.quit()



#driver.get("https://the-internet.herokuapp.com/checkboxes")

#divs = driver.find_elements(By.CSS_SELECTOR, "div")

#div = divs[6]
#запрашиваем атрибуты и помещаем в переменную css_class:
#css_class = div.get_attribute("class")
#выводим в терминал:
#print(css_class)



from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/checkboxes")

# Используйте find_elements для получения списка элементов
divs = browser.find_elements(By.CSS_SELECTOR, "div")

# Теперь можно обратиться к элементу по индексу
div = divs[6]
css_class = div.get_attribute("class")

print(css_class)

browser.quit()