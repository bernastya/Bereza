from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop_total():
    # 1. Открываем сайт в Firefox
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавление товаров в корзину
        # Используем локаторы для кнопок добавления конкретных товаров
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        
        for item_id in items_to_add:
            driver.find_element(By.ID, item_id).click()

        # 4. Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Нажимаем Checkout
        driver.find_element(By.ID, "checkout").click()

        # 6. Заполнение формы данными
        driver.find_element(By.ID, "first-name").send_keys("Анастасия")
        driver.find_element(By.ID, "last-name").send_keys("Береза")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # 7. Нажимаем кнопку Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Читаем итоговую стоимость (Total)
        # Ищем элемент с классом summary_total_label
        total_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text  # Получим строку вида "Total: $58.29"

        # 9. Проверка итоговой суммы
        # Ожидаемая сумма: $58.29
        assert "58.29" in total_text, f"Ожидалась сумма $58.29, но получили: {total_text}"
        
        print(f"Тест пройден успешно! {total_text}")

    finally:
        # 10. Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_shop_total()
