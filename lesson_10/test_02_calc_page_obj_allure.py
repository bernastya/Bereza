from selenium import webdriver
from CalcPage_allure import CalcPage
import allure


@allure.epic("Калькулятор")
@allure.severity("critical")
@allure.title("Проверка функциоанльностикалькулятора")
@allure.description("Этот тест выполняет проверку корректности \
                     вычислений на калькуляторе с задежржкой")
@allure.feature("Вычисления на калькуляторе")
def test_calc():
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome()
    with allure.step("Открытие страницы калькулятора"):
        calc_page = CalcPage(driver)
    with allure.step("Настройка задержки"):
        calc_page.delay(45)
    with allure.step("Нажатие кнопок"):
        calc_page.click_buttons('7', '+', '8', '=')
    with allure.step("Ожидание и получение результата"):
        as_is = calc_page.get_result("15")
    with allure.step("Сравнение результата с ожидаемым"):
        assert as_is == "15"
    with allure.step("Закрытие браузера"):
        calc_page.close_driver()
