from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def login(self, name, password):
        self.driver.find_element(By.ID, "user-name").send_keys(name)
        self.driver.find_element(By.ID, "password").send_keys(password)

    def button(self):
        self.driver.find_element(By.ID, "login-button").click()
