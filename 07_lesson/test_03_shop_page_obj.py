from selenium import webdriver
from ShopPageLog_in import Log_in
from ShopPageItems import Items
from ShopPageCheckout import Checkout
from ShopPageTotal import Total


def test_shop():
    driver = webdriver.Firefox()
    log_in_page = Log_in(driver)
    log_in_page.login("standard_user", "secret_sauce")
    log_in_page.button()
    items_page = Items(driver)
    items_page.items()
    items_page.shopping_cart()
    checkout = Checkout(driver)
    checkout.checkout()
    total_page = Total(driver)
    total_page.name("Анастасия", "Береза", "123456")
    as_is = total_page.summary("58.29")
    assert as_is == "Total: $58.29"
    total_page.close_driver()
