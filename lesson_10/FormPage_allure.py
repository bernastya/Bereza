from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:

    def __init__(self, driver):
        """
        Конструктор класса FormPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :return: None
        Открывает сайт для тестирования.
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение полей ввода {first_name}, {last_name}, {address}, \
                 {zip_code}, {city}, {country}, {e_mail}, {phone},\
                 {job_position},{company}")
    def name(self, first_name, last_name, address, zip_code,
             city, country, e_mail, phone, job_position, company):
        """Заполняет поля ввода значениями:
        :param first_name: str - Имя,
        :param last_name: str - Фамилия,
        :param address: str - Адрес,
        :param zip-code: str - Индекс,
        :param city: str - Город,
        :param country: str - Страна,
        :param e_mail: str - адрес электронной почты,
        :param phone: str - телефон,
        :param job_position: str - должность,
        :param company: str - место работы.
        :return: None
        """
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
        """Ожидает что кнопка становится кликабельной и нажимает на нее"""
        wait = WebDriverWait(self.driver, 30)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")))
        self.driver.execute_script("arguments[0].click();", button)

    def chek_color_red(self):
        """ Ожидает появления поля zip-code в DOM.
        :return: WebElement — объект элемента zip-code."""
        wait = WebDriverWait(self.driver, 30)
        self.zip_code_container = wait.until(EC.presence_of_element_located(
            (By.ID, "zip-code")))
        return self.zip_code_container

    def color_red(self):
        """ Получает CSS-класс поля zip-code.
        :return: str — название классов элемента ('alert-danger').
        """
        return self.driver.find_element(By.ID,
                                        "zip-code").get_attribute("class")

    def color_green(self):
        """
        Получает CSS-классы всех заполненных полей.
        :return: list — список строк (классов) для каждого поля.
        """

        fields = ["first-name", "last-name", "address", "city", "country",
                  "e-mail", "phone", "job-position", "company"]
        return [self.driver.find_element(By.ID, f).get_attribute("class")
                for f in fields]

    def close_driver(self):
        """ Закрывает браузер по окончании теста
        :return: None"""
        self.driver.quit()
