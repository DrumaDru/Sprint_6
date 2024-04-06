import pytest
import allure
from Sprint_6.pages.order_page import OrderPage
from Sprint_6.pages.main_page import MainPage
from Sprint_6.pages.dzen_page import DzenPage


class TestPositiveOrders:
    @allure.title('Проверяем, что, после заполнения формы заказа самоката, первым набором тестовых данных,'
                  'появляется модальное окно с номером заказа')
    @allure.description('На странице заполнения второй части формы, проверяем, что открылось модальное окно,с номером заказа,'
                        'в котором есть кнопка с текстом "Посмотреть статус"')
    def test_positive_order_one(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.make_order_head_button()
        modal_success = order_page.positive_order_one()

        assert modal_success.text == 'Посмотреть статус'

    @allure.title('Проверяем, что после нажатия на кнопку "Посмотреть статус" и нажатия на гиперссылку "Самокат",'
                  'на странице с данными о заказе, просходит переход на главную страницу сервиса Яндекс.Самокат')
    @allure.description('После перехода по гиперссылке "Самокат", проверям на главной странице сервиса Яндекс.Самокат,'
                        'наличие заголовка, который содержит такст "Самокат"')
    def test_check_scooter_link(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.make_order_head_button()
        order_page.switch_to_order_page()
        title_text = order_page.scooter_button()

        assert 'Самокат' in title_text

    @allure.title('Проверяем, что, после заполнения формы заказа самоката, вторым набором тестовых данных,'
                  'появляется модальное окно с номером заказа')
    @allure.description('На странице заполнения второй части формы, проверяем, что открылось модальное окно,с номером заказа,'
                        'в котором есть кнопка с текстом "Посмотреть статус"')
    def test_positive_order_two(self, driver):
         main_page = MainPage(driver)
         order_page = OrderPage(driver)

         main_page.make_order_foot_button()
         modal_success = order_page.positive_order_two()

         assert modal_success.text == 'Посмотреть статус'

    @allure.title('Проверяем, что после нажатия на кнопку "Посмотреть статус" и нажатия на гиперссылку "Яндекс",'
                  'на странице с данными о заказе, просходит переход на главную страницу "Дзен"')
    @allure.description('После перехода по гиперссылке "Яндекс", проверям на главной странице "Дзен",'
                        'наличие элемента, который содержит такст "Главная"')
    def test_check_yandex_link(self, driver):
        order_page = OrderPage(driver)
        dzen_page = DzenPage(driver)
        main_page = MainPage(driver)

        main_page.make_order_foot_button()
        order_page.switch_to_order_page()
        title_text = dzen_page.check_dzen_page()

        assert "Главная" in title_text