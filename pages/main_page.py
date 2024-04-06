import allure
from Sprint_6.pages.base_page import BasePage
from Sprint_6.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    cookies_button = MainPageLocators.COOKIES_BUTTON
    order_button_head = MainPageLocators.ORDER_BUTTON_HEAD
    order_button_foot = MainPageLocators.ORDER_BUTTON_FOOT

    @allure.step('Создаем метод, который использует методы format_locators, для передачи локатора и номера num,'
                 'click_to_element, для клика по элементам и get_text_from_element, для получения текста элемента')
    def get_answer_text(self, locator_q, locator_a, num):
        question_element_formatted = self.format_locators(locator_q, num)
        answer_element_formatted = self.format_locators(locator_a, num)
        self.click_to_element(self.cookies_button)
        self.click_to_element(question_element_formatted)
        return self.get_text_from_element(answer_element_formatted)

    @allure.step('Создаем метод, который использует метод click_to_element, для поиска верхней кнопки "Заказать" на странице'
                 'и клика по ней')
    def make_order_head_button(self):
        self.click_to_element(self.order_button_head)

    @allure.step('Создаем метод, который использует методы scroll_into_view_element, для поиска нижней кнопки "Заказать",'
                 'и click_to_element, для поиска верхней кнопки "Заказать" на странице и клика по ней')
    def make_order_foot_button(self):
        self.click_to_element(self.cookies_button)
        self.scroll_into_view_element(self.order_button_foot)
        self.click_to_element(self.order_button_foot)




