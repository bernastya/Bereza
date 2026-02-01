from selenium import webdriver
from ShopPageLog_in import LoginPage
from ShopPageItems import ItemsPage
from ShopPageCheckout import CheckoutPage
from ShopPageTotal import TotalPage


def test_shop():
    driver = webdriver.Firefox()
    log_in_page = LoginPage(driver)
    log_in_page.login("standard_user", "secret_sauce")
    log_in_page.button()
    items_page = ItemsPage(driver)
    items_page.items()
    items_page.shopping_cart()
    checkout = CheckoutPage(driver)
    checkout.checkout()
    total_page = TotalPage(driver)
    total_page.name("Анастасия", "Береза", "123456")
    as_is = total_page.summary("58.29")
    assert as_is == "Total: $58.29"
    total_page.close_driver()
