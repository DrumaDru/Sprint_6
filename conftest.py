import pytest
from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions


@pytest.fixture(scope="function")
def driver():
    opts = FirefoxOptions()
    opts.add_argument("--width=1920")
    opts.add_argument("--height=1080")
    driver = webdriver.Firefox(options=opts)
    #Открываем веб-страницу
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    #выходим из браузера
    driver.quit()


