from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# 1. Жесткая настройка браузера против переводчиков и логов
options = webdriver.ChromeOptions()
options.add_argument("--disable-features=Translate") # Отключить перевод
options.add_argument("--start-maximized")            # На весь экран
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

def test_calc():
    # 2. Открываем сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Ждем появления поля delay (базовый элемент)
    wait = WebDriverWait(driver, 20)
    delay_input = wait.until(EC.element_to_be_clickable((By.ID, "delay")))
    
    # 3. Очистка и ввод 45
    delay_input.send_keys(Keys.CONTROL + "a")
    delay_input.send_keys(Keys.BACKSPACE)
    delay_input.send_keys("45")

    # 4. Нажимаем кнопки через ActionChains
    # ВНИМАНИЕ: используем упрощенный селектор без привязки к тегу span
    actions = ActionChains(driver)
    
    # Список кнопок для нажатия
    for val in ['7', '+', '8', '=']:
        # Ищем любой элемент, у которого есть атрибут data-value
        # Это сработает, даже если переводчик изменил теги внутри
        selector = f"[data-value='{val}']"
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        actions.move_to_element(element).click().perform()

    # 5. Ожидание результата (45 секунд задержки + запас)
    # Ждем, пока в окне с классом "screen" появится текст "15"
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # 6. Финальная проверка
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"
    print(f"Успех! Получен результат: {result}")

try:
    test_calc()
finally:
    driver.quit()