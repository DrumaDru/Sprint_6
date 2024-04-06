import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    @allure.step('Принимаем экземпляр драйвера и сохраняем его в атрибут self.driver')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Создаем метод, который содержит в себе условное ожидание, пока элемент не станет видимым'
                 'и метод класса WebDriver - find_element')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Создаем метод, который содержит в себе условное ожидание, пока элемент не станет кликабильным'
                 'и выполяем клик, по элементу, с использованием метода класса WebDriver- find_element')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Создаем метод с и использованием метода класса WebDriver - end_keys, который добавляет текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Создаем метод, который использует метод класса find_element_with_wait для получения текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Создаем метод, который использует метод класса WebDriver - click_to_element, для перехода по элементу,'
                 'сохраняем в переменную windows, кол-во открытых вкладок,'
                 'используем условное ожидание, для проверки, что в браузере была открыта новая вкладка,'
                 'и с помощьюу метода класса WebDriver switch_to, переходим на новую вкладку')
    def switch_to_new_tab(self, locator_1):
        self.click_to_element(locator_1)
        # Получаем список всех открытых вкладок
        windows = self.driver.window_handles
        # Ждем появления новой вкладки
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
            # Переключаемся на последнюю (новую) вкладку
        self.driver.switch_to.window(windows[-1])

    @allure.step('Создаем метод, который используется для динамической подстановки значения num в строку локатора')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return (method, locator)

    @allure.step('Создаем метод, который перемещается до переданного локатора на странице браузера')
    def scroll_into_view_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

