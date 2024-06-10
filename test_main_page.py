import pytest
from selenium import webdriver
from pages.MainPage import MainPage

# Параметры для теста
URL = "http://example.com"

@pytest.fixture
def browser():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_open_main_page(browser):
    # Создание объекта страницы
    main_page = MainPage(browser, URL)
    
    # Открытие страницы
    main_page.open()
    
    # Добавьте проверки, чтобы удостовериться, что страница открыта правильно
    assert "Example Domain" in browser.title
