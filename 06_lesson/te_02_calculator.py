from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

def test_calc():
    # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 30)
    # 2. Находим поле задержки, очищаем и вводим 45
    delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()  
    delay_input.send_keys("45")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='7']"))).click()

    # 3. Нажимаем кнопки
    # ОШИБКА БЫЛА ТУТ: data-value — это атрибут, поэтому используем CSS_SELECTOR, а не CLASS_NAME
    driver.find_element(By.CSS_SELECTOR, 'span[data-value="+"]').click()
    driver.find_element(By.CSS_SELECTOR, 'span[data-value="8"]').click()
    driver.find_element(By.CSS_SELECTOR, 'span[data-value="="]').click()

    # 4. Ожидание результата
    # Создаем объект ожидания. Ставим 50 секунд, так как задержка на сайте 45.
    wait = WebDriverWait(driver, 50)
    
    # Ждем, пока в элементе с классом "screen" появится текст "15"
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    # 5. Проверка результата
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"
    print(f"Тест пройден! Результат: {result}")

# Запуск теста
try:
    test_calc()
finally:
    # Закрываем браузер
    driver.quit()

