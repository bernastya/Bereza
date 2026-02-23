from selenium import webdriver
from ShopPageLog_in_allure import LoginPage
from ShopPageItems_allure import ItemsPage
from ShopPageCheckout_allure import CheckoutPage
from ShopPageTotal_allure import TotalPage
import allure


@allure.epic("Интернет-магазин")
@allure.severity("critical")
@allure.title("Проверка основной функциональности интернет-магазина")
@allure.description("Этот тест выполняет проверку авторизации, \
                    добавления в корзину товаров и итоговой суммы покупки")
@allure.feature("Покупка товаров в магазине")
def test_shop():
    with allure.step("Подготовка и вход"):
        with allure.step("Запуск браузера Firefox"):
            driver = webdriver.Firefox()
        with allure.step("Введение логина и пароля пользователя"):
            log_in_page = LoginPage(driver)
            log_in_page.login("standard_user", "secret_sauce")
        with allure.step("Нажатие кнопки Login для входа в систему"):
            log_in_page.button()
    with allure.step("Выбор товаров"):
        with allure.step("Добавление в корзину товаров по их ID"):
            items_page = ItemsPage(driver)
            items_page.items()
        with allure.step("Клик по иконке корзины"):
            items_page.shopping_cart()
    with allure.step("Нажатие кнопки Checkout"):
        checkout = CheckoutPage(driver)
        checkout.checkout()
    with allure.step("Ввод данных и проверка суммы"):
        with allure.step("Заполняет форму"):
            total_page = TotalPage(driver)
            total_page.name("Анастасия", "Береза", "123456")
        with allure.step("Ожидание появления суммы"):
            as_is = total_page.summary()
        with allure.step("Сравнение появившейся суммы с ожидаемой"):
            assert as_is == "Total: $58.29"
    with allure.step("Закрытие браузера"):
        total_page.close_driver()
