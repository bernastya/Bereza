from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():

    driver = webdriver.Chrome()

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        wait = WebDriverWait(driver, 55)

        delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                             "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//span[text()='7']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//span[text()='+']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//span[text()='8']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//span[text()='=']"))).click()
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,
                                                     "screen"), "15"))

        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15"
        print(f"Тест успешно пройден! Результат: {result}")

    except Exception as e:
        print(f"Тест не пройден: {e}")
    finally:

        driver.quit()


if __name__ == "__main__":
    test_calc()
