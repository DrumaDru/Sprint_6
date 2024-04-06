import allure
from Sprint_6.pages.order_page import OrderPage
from Sprint_6.pages.base_page import BasePage
from Sprint_6.locators.dzen_locators import DzenLocators

class DzenPage(OrderPage, BasePage):
    tab_main = DzenLocators.TAB_MAIN

    @allure.step('Создаем метод, который преключается на страницу "Дзен" и с помощью метода WebDriver- get_text_from_element,'
                 'получает текст вкладки "Главная"')
    def check_dzen_page(self):
        self.switch_to_dzen_top()
        return self.get_text_from_element(self.tab_main)


