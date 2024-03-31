from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_ELEMENT = By.ID, 'accordion__heading-{}'
    ANSWER_ELEMENT = By.ID, 'accordion__panel-{}'
    ORDER_BUTTON_HEAD = By.CLASS_NAME, "Button_Button__ra12g"
    ORDER_BUTTON_FOOT =By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM"
    YANDEX_LINK = By.XPATH, ".//*[@alt='Yandex']"
    SCOOTER_LINK = By.XPATH, ".//*[@alt='Scooter']"
