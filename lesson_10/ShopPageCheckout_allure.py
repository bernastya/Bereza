from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :return: None
        """
        self.driver = driver

    def checkout(self):
        """Находит кнопку с ID checkout и кликает по ней.
        :return: None"""
        self.driver.find_element(By.ID, "checkout").click()
