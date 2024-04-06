from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIES_BUTTON = By.ID, 'rcc-confirm-button'
    QUESTION_ELEMENT = By.ID, 'accordion__heading-{}'
    ANSWER_ELEMENT = By.ID, 'accordion__panel-{}'
    ORDER_BUTTON_HEAD = By.XPATH, ".//div/button[@class = 'Button_Button__ra12g' and text() = 'Заказать']"
    ORDER_BUTTON_FOOT = By.XPATH, ".//div/button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']"
    HEAD_TITLE = By.CLASS_NAME, 'Home_Header__iJKdX'


