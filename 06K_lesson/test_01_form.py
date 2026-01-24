from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():

    driver = webdriver.Edge()

    driver.implicitly_wait(10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR,
                        '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="company"]').send_keys("SkyPro")

    wait = WebDriverWait(driver, 30)
    button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")))

    driver.execute_script("arguments[0].click();", button)

    zip_code_container = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")))
    assert "alert-danger" in zip_code_container.get_attribute("class"), (
        "Поле Zip code не подсвечено красным!"
    )
    print("Проверка Zip Code (red) пройдена!")

    success_fields = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in success_fields:
        element = driver.find_element(By.ID, field_id)
        classes = element.get_attribute("class")
        assert "alert-success" in classes, (
            f"Поле {field_id} не подсвечено зеленым! "
            f"Классы: {classes}"
        )
        print(f"Поле {field_id} подсвечено зеленым.")

    print("Все тесты успешно пройдены!")

    driver.quit()


test_form()
