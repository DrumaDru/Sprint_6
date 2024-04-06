import allure
from Sprint_6.pages.base_page import BasePage
from Sprint_6.locators.order_page_locators import OrderPageLocators
from Sprint_6.locators.main_page_locators import MainPageLocators
import test_data


class OrderPage(BasePage):
    yandex_link = OrderPageLocators.YANDEX_LINK
    scooter_link = OrderPageLocators.SCOOTER_LINK
    name = OrderPageLocators.NAME
    surname = OrderPageLocators.SURNAME
    address = OrderPageLocators.ADDRESS
    input_metro = OrderPageLocators.INPUT_METRO
    metro_station_first = OrderPageLocators.METRO_STATION_FIRST
    metro_station_second = OrderPageLocators.METRO_STATION_SECOND
    phone = OrderPageLocators.PHONE
    button_next = OrderPageLocators.BUTTON_NEXT
    second_title = OrderPageLocators.SECOND_PAGE_TITLE
    date = OrderPageLocators.DATE
    date_picker = OrderPageLocators.DATE_PICKER
    selected_day = OrderPageLocators.SELECTED_DAY
    duration = OrderPageLocators.DURATION
    one_day = OrderPageLocators.ONE_DAY
    two_day = OrderPageLocators.TWO_DAY
    black_check_box = OrderPageLocators.BLACK_CHECK_BOX
    grey_check_box = OrderPageLocators.GREY_CHECK_BOX
    button_order = OrderPageLocators.BUTTON_ORDER
    modal_order = OrderPageLocators.MODAL_ORDER
    button_yes = OrderPageLocators.BUTTON_YES
    modal_success = OrderPageLocators.MODAL_SUCCESS
    check_status = OrderPageLocators.CHECK_STATUS
    head_title = MainPageLocators.HEAD_TITLE
    order_button = MainPageLocators.ORDER_BUTTON_HEAD

    @allure.step('Создаем метод, который использует метод класса WebDriver-click_to_element, для поиска и нажатия'
                 'на гиперссылку "Самокат"')
    def scooter_button(self):
        self.click_to_element(self.scooter_link)
        return self.get_text_from_element(self.head_title)

    @allure.step('Создаем метод, который использует метод switch_to_new_tab, для перехода по гиперссылке "Яндекс",'
                 'на страницу "Дзен"')
    def switch_to_dzen_top(self):
        self.switch_to_new_tab(self.yandex_link)

    @allure.step('Создаем метод, для заполнения формы аренды самоката, с первым набором тестовых данных '
                 'и передачи локатора кнопки "Посмотреть статус"')
    def positive_order_one(self):
        self.add_text_to_element(self.name, test_data.name)
        self.add_text_to_element(self.surname, test_data.surname)
        self.add_text_to_element(self.address, test_data.address)
        self.click_to_element(self.input_metro)
        self.scroll_into_view_element(self.metro_station_first)
        self.click_to_element(self.metro_station_first)
        self.add_text_to_element(self.phone, test_data.phone)
        self.click_to_element(self.button_next)
        self.find_element_with_wait(self.second_title)
        self.add_text_to_element(self.date, test_data.today_date)
        self.click_to_element(self.selected_day)
        self.click_to_element(self.duration)
        self.click_to_element(self.one_day)
        self.click_to_element(self.black_check_box)
        self.click_to_element(self.button_order)
        self.find_element_with_wait(self.modal_order)
        self.click_to_element(self.button_yes)
        return self.find_element_with_wait(self.check_status)

    @allure.step('Создаем метод, для заполнения формы аренды самоката, со вторым набором тестовых данных '
                 'и передачи локатора кнопки "Посмотреть статус"')
    def positive_order_two(self):
        self.add_text_to_element(self.name, test_data.name_2)
        self.add_text_to_element(self.surname, test_data.surname_2)
        self.add_text_to_element(self.address, test_data.address_2)
        self.click_to_element(self.input_metro)
        self.scroll_into_view_element(self.metro_station_second)
        self.click_to_element(self.metro_station_second)
        self.add_text_to_element(self.phone, test_data.phone)
        self.click_to_element(self.button_next)
        self.find_element_with_wait(self.second_title)
        self.add_text_to_element(self.date, test_data.tomorrow_date)
        self.click_to_element(self.selected_day)
        self.click_to_element(self.duration)
        self.click_to_element(self.one_day)
        self.click_to_element(self.black_check_box)
        self.click_to_element(self.button_order)
        self.find_element_with_wait(self.modal_order)
        self.click_to_element(self.button_yes)
        return self.find_element_with_wait(self.check_status)


    def switch_to_order_page(self):
        look_status_button = self.positive_order_one()
        look_status_button.click()

