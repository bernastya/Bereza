from selenium.webdriver.common.by import By
import allure


class LoginPage:

    def __init__(self, driver):
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :return: None
        Открывает сайт для тестирования.
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Заполнение полей ввода {name}, {password}")
    def login(self, name, password):
        """Заполняет поля ввода значениями:
        :param name: str - Имя пользователя,
        :param password: str - Пароль пользователя.
        :return: None"""
        self.driver.find_element(By.ID, "user-name").send_keys(name)
        self.driver.find_element(By.ID, "password").send_keys(password)

    def button(self):
        """Находит кнопку Login по ID и кликает по ней.
        :return: None"""
        self.driver.find_element(By.ID, "login-button").click()
