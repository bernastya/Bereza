from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

def test_calc():
    try:
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Создаем один объект ожидания на 50 секунд
        wait = WebDriverWait(driver, 50)

        # 2. Находим поле задержки, очищаем и вводим 45
        delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()  
        delay_input.send_keys("45")

        # 3. Нажимаем кнопки (Исправлены селекторы: используем 'operator' и 'btn-outline-primary')
        # Нажимаем "7"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
        
        # Нажимаем "+" (На сайте это кнопки с текстом или определенным классом)
        # В данном калькуляторе кнопки - это span с текстом внутри кнопок
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
        
        # Нажимаем "8"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
        
        # Нажимаем "="
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()

        # 4. Ожидание результата
        # Ждем, пока в элементе с классом "screen" появится текст "15"
        # Индикатор выполнения (спиннер) исчезнет, и появится число
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        # 5. Проверка результата
        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15"
        print(f"Тест пройден успешно! Результат: {result}")

    except Exception as e:
        print(f"Тест провален: {e}")
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_calc()