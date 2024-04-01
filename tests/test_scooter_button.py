import pytest
from Sprint_6.pages.order_page import OrderPage
from Sprint_6.locators.order_page_locators import OrderPageLocators
from Sprint_6.locators.main_page_locators import MainPageLocators

class TestScooterButton:

    def test_scooter_button(self, driver):
        order_page = OrderPage(driver)
        assert 'Самокат' in order_page.scooter_button(
            MainPageLocators.ORDER_BUTTON_HEAD,
            OrderPageLocators.SCOOTER_LINK,
            MainPageLocators.HEAD_TITLE
        )
