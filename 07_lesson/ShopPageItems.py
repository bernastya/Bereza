from selenium.webdriver.common.by import By


class ItemsPage:

    def __init__(self, driver):
        self.driver = driver

    def items(self):
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for item_id in items_to_add:
            self.driver.find_element(By.ID, item_id).click()

    def shopping_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
