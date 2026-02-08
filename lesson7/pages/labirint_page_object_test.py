from selenium import webdriver
from pages.main_page import MainPage
from pages.result_page import ResultPage
from pages.cart_page import CartPage


def test_cart_counter():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) # Рекомендуется добавить неявное ожидание
    try:
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        main_page.search("Python")

        result_page = ResultPage(browser)
        to_be = result_page.add_books()

        cart_page = CartPage(browser)
        cart_page.get()
        as_is = cart_page.get_counter()

        assert as_is == to_be, f"Ожидалось {to_be}, но получили {as_is}"
    finally:
        browser.quit()