from selenium import webdriver
from CalcPage import CalcPage


def test_calc():
    driver = webdriver.Chrome()
    calc_page = CalcPage(driver)
    calc_page.delay(45)
    calc_page.buttons('7', '+', '8', '=')
    as_is = calc_page.get_result("15")
    assert as_is == "15"
    calc_page.close_driver()
