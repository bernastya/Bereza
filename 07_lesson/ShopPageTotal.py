from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TotalPage:

    def __init__(self, driver):
        self.driver = driver

    def name(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def summary(self, total):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        ))
        return self.driver.find_element(By.CLASS_NAME,
                                        "summary_total_label").text

    def close_driver(self):
        self.driver.quit()
