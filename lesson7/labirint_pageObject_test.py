from selenium import webdriver
from pages.main_page import MainPage
from pages.result_page import ResultPage
from pages.cart_page import CartPage


def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = MainPage(browser) 
    main_page.set_cookie_policy()
    main_page.search("Python")

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  # Используем только в видео
    to_be = result_page.add_books()  # Результат вызова add_books

    cart_page = CartPage(browser)
    cart_page.get()  # Переход на страницу с корзиной
    as_is = cart_page.get_counter()  # Текущее значение счетчика на странице 

    assert as_is == to_be

    browser.quit()