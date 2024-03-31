from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = By.XPATH, ".//*[@placeholder = '* Имя']"
    SURNAME = By.XPATH, ".//*[@placeholder = '* Фамилия']"
    ADDRESS = By.XPATH, ".//*[@placeholder = '* Адрес: куда привезти заказ']"
    METRO_STATION = By.CLASS_NAME, "select-search__input"
    PHONE = By.XPATH, ".//*[@placeholder = '* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, ".//*[text()='Далее']"
    DATE = By.XPATH, ".//*[@placeholder = '* Когда привезти самокат']"git
    DURATION = By.CLASS_NAME, 'Dropdown-placeholder'
    BLACK_CHECK_BOX = By.ID, 'black'
    GREY_CHECK_BOX = By.ID, 'grey'
    BUTTON_ORDER = By.XPATH, ".//*[text()='Заказать']"
    MODAL_ORDER = By.CLASS_NAME, "Order_Modal__YZ-d3"
    BUTTON_YES = By.XPATH, ".//*[text()='Да']"
    MODAL_SUCCESS_ORDER = By.XPATH, ".//*[text()='Да']"
