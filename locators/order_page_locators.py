from selenium.webdriver.common.by import By

class OrderPageLocators:
    SCOOTER_LINK = By.XPATH, ".//img[@alt = 'Scooter']/parent::a[@class ='Header_LogoScooter__3lsAR']"
    YANDEX_LINK = By.XPATH, ".//*[@alt='Yandex']"
    NAME = By.XPATH, ".//*[@placeholder = '* Имя']"
    SURNAME = By.XPATH, ".//*[@placeholder = '* Фамилия']"
    ADDRESS = By.XPATH, ".//*[@placeholder = '* Адрес: куда привезти заказ']"
    INPUT_METRO = By.XPATH, ".//input[@class ='select-search__input' and @placeholder = '* Станция метро']"
    METRO_STATION_FIRST = By.XPATH, ".//button[@class = 'Order_SelectOption__82bhS select-search__option' and @value = '21']"
    METRO_STATION_SECOND = By.XPATH, ".//button[@class = 'Order_SelectOption__82bhS select-search__option' and @value = '22']"
    PHONE = By.XPATH, ".//*[@placeholder = '* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, ".//*[text()='Далее']"
    SECOND_PAGE_TITLE = By.XPATH, ".//*[text() = 'Про аренду']"
    DATE = By.XPATH, ".//*[@placeholder = '* Когда привезти самокат']"
    DATE_PICKER = By.CLASS_NAME, "react-datepicker__current-month"
    SELECTED_DAY = By.XPATH, ".//*[contains(@class, 'react-datepicker__day--selected')]"
    DURATION = By.CLASS_NAME, 'Dropdown-placeholder'
    ONE_DAY = By.XPATH, ".//*[text() ='сутки']"
    TWO_DAY = By.XPATH, ".//*[text() ='двое суток'"
    BLACK_CHECK_BOX = By.ID, 'black'
    GREY_CHECK_BOX = By.ID, 'grey'
    BUTTON_ORDER = By.XPATH, ".//div/button[@class ='Button_Button__ra12g Button_Middle__1CSJM' and text()= 'Заказать']"
    MODAL_ORDER = By.CLASS_NAME, "Order_Modal__YZ-d3"
    BUTTON_YES = By.XPATH, ".//*[text()='Да']"
    MODAL_SUCCESS = By.XPATH, ".//div/div[@class = 'Order_ModalHeader__3FDaJ' and text() = 'Заказ оформлен']"
    CHECK_STATUS = By.XPATH, ".//*[text() = 'Посмотреть статус']"

