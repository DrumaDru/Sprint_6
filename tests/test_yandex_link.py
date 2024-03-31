import pytest
from Sprint_6.pages.main_page import MainPage
from Sprint_6.locators.main_page_locators import MainPageLocators
from Sprint_6.locators.dzen_locators import DzenLocators


class TestYandexLink:

    def test_yandex_link(self, driver):
        main_page = MainPage(driver)
        assert main_page.get_dzen(
            MainPageLocators.YANDEX_LINK,
            DzenLocators.INPUT_SEARCH
        ) == DzenLocators.INPUT_SEARCH


