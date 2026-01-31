
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self, time):
        wait = WebDriverWait(self.driver, 10)
        delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                             "#delay")))
        delay_input.clear()
        delay_input.send_keys(time)

    def buttons(self, *args):
        wait = WebDriverWait(self.driver, 10)
        for char in args:
            locator = (By.XPATH, f"//span[text()='{char}']")
            wait.until(EC.element_to_be_clickable(locator)).click()

    def get_result(self, expected_value):
        expected_value = str(expected_value)
        wait = WebDriverWait(self.driver, 55)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), expected_value)
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    def close_driver(self):
        self.driver.quit()
