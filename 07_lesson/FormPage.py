from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def name(self, first_name, last_name, address, zip_code,
             city, country, e_mail, phone, job_position, company):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="first-name"]').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="last-name"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="zip-code"]').send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="e-mail"]').send_keys(e_mail)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="phone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="job-position"]').send_keys(
                                     job_position)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[name="company"]').send_keys(company)

    def button(self):
        wait = WebDriverWait(self.driver, 30)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")))
        self.driver.execute_script("arguments[0].click();", button)

    def chek_color_red(self):
        wait = WebDriverWait(self.driver, 30)
        self.zip_code_container = wait.until(EC.presence_of_element_located(
            (By.ID, "zip-code")))
        return self.zip_code_container

    def color_red(self):
        wait = WebDriverWait(self.driver, 30)
        self.zip_code_container = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code")))
        return self.zip_code_container

    def color_green(self):
        self.success_elements = []
        success_fields = ["first-name", "last-name", "address",
                          "city", "country", "e-mail", "phone",
                          "job-position", "company"]
        for field_id in success_fields:
            element = self.driver.find_element(By.ID, field_id)
            self.success_elements.append(element)
            return self.success_elements

    def chek(self):
        assert "alert-danger" in self.zip_code_container.get_attribute(
            "class"), "Zip code не красный!"

        for element in self.success_elements:
            classes = element.get_attribute("class")
            assert "alert-success" in classes, (
                f"Поле {element.get_attribute('id')} не зеленое! "
                f"Классы: {classes}"
            )

    def close_driver(self):
        self.driver.quit()
