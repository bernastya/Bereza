from selenium import webdriver
from FormPage_allure import FormPage
import allure


@allure.epic("Форма заполнения")
@allure.severity("critikal")
@allure.title("Проверка формы заполнения")
@allure.description("Этот тест выполняет проверку "
                    "подсветки полей разными цветами после её отправки.")
@allure.feature("Валидация формы")
def test_form():
    with allure.step("Запуск браузера Microsoft Edge"):
        driver = webdriver.Edge()
        form_page = FormPage(driver)
    with allure.step("Заполнение полей"):
        form_page.name("Иван", "Петров", "Ленина, 55-3", "",
                       "Москва", "Россия", "test@skypro.com",
                       "+7985899998787", "QA", "SkyPro")
    with allure.step("Нажатие кнопки отправки формы"):
        form_page.button()
    with allure.step("Получение CSS-класса поля Zip-code"):
        zip_classes = form_page.color_red()
    with allure.step("Проверка, что это поле подсвечено красным цветом"):
        assert "alert-danger" in zip_classes
    with allure.step("Проверка, что все остальные поля \
                     подсвечены зеленым цветом"):
        for classes in form_page.color_green():
            assert "alert-success" in classes
    with allure.step("Закрытие браузера"):
        form_page.close_driver()
