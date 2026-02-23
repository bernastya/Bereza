from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:

    def __init__(self, driver):
        """
        Конструктор класса CalcPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :return: None
        Открывает сайт для тестирования.
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки {time} сек.")
    def delay(self, time):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param time: int — время задержки в секундах.
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        delay_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                             "#delay")))
        delay_input.clear()
        delay_input.send_keys(time)

    @allure.step("Нажатие кнопок: {buttons}")
    def click_buttons(self, *buttons):
        """
        Нажимает последовательность кнопок на калькуляторе.
        :param buttons: str — произвольное количество
        текстовых символов кнопок.
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        for char in buttons:
            locator = (By.XPATH, f"//span[text()='{char}']")
            wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ожидание и получение результата: {expected_value}")
    def get_result(self, expected_value):
        """
        Ожидает появления конкретного значения на экране в
        течение 55 секунд и возвращает его.
        :param expected_value: str — значение, которое мы рассчитываем увидеть.
        :return: str — результат с экрана калькулятора.
        """
        expected_value = str(expected_value)
        wait = WebDriverWait(self.driver, 55)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), expected_value)
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    def close_driver(self):
        """ Закрывает браузер по окончании теста
        :return: None"""
        self.driver.quit()
