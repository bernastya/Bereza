from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():

    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for item_id in items_to_add:
            driver.find_element(By.ID, item_id).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Анастасия")
        driver.find_element(By.ID, "last-name").send_keys("Береза")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            "summary_total_label"))
        )
        total = element.text

        assert "58.29" in total, (
            f"Ожидалась сумма $58.29, но получили: {total}"
        )

        print(f"Тест успешно пройден! {total}")

    finally:

        driver.quit()


if __name__ == "__main__":
    test_shop()
