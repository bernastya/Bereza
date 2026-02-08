from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2. Создаем драйвер
driver = webdriver.Edge()


def open_bonigarcia():
    driver.implicitly_wait(20)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    

def name(first_name, last_name, address, zip_code, city, country, e_mail, phone, job_position, company):
    driver.find_element(By.CSS_SELECTOR,
                        '[name="first-name"]').send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="last-name"]').send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="address"]').send_keys(address)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="zip-code"]').send_keys(zip_code)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="city"]').send_keys(city)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="country"]').send_keys(country)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="e-mail"]').send_keys(e_mail)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="phone"]').send_keys(phone)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="job-position"]').send_keys(job_position)
    driver.find_element(By.CSS_SELECTOR,
                        '[name="company"]').send_keys(company)


def button():
    wait = WebDriverWait(driver, 30)
    button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")))
    driver.execute_script("arguments[0].click();", button)


def chek_color_red():
    wait = WebDriverWait(driver, 30)
    zip_code_container = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")))
    assert "alert-danger" in zip_code_container.get_attribute("class"), (
        "Поле Zip code не подсвечено красным!"
    )
    print("Проверка Zip Code (red) пройдена!")


def chek_color_green():

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
    

def close_driver():
    driver.quit()


def test_form():
    open_bonigarcia()
    name("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", 
         "test@skypro.com", "+7985899998787", "QA", "SkyPro")
    button()
    chek_color_red()
    chek_color_green()
    print("Все тесты успешно пройдены!")
    close_driver()
 
