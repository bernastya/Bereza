from selenium import webdriver
from FormPage import FormPage


def test_form():
    driver = webdriver.Edge()
    form_page = FormPage(driver)
    form_page.name("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия",
                   "test@skypro.com", "+7985899998787", "QA", "SkyPro")
    form_page.button()
    zip_classes = form_page.color_red()
    assert "alert-danger" in zip_classes
    for classes in form_page.color_green():
        assert "alert-success" in classes
    form_page.close_driver()
