from selenium.webdriver.common.by import By
import allure


class ItemsPage:

    def __init__(self, driver):
        """
        Конструктор класса ItemsPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :return: None
        """
        self.driver = driver

    @allure.step("Находит товары по ID и кликает по ним")
    def items(self):
        """Находит кнопки добавления товаров по ID и кликает по ним.
        :return: None"""
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for item_id in items_to_add:
            self.driver.find_element(By.ID, item_id).click()

    def shopping_cart(self):
        """Кликает по иконке корзины.
        :return: None"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
