import pytest
from Sprint_6.pages.main_page import MainPage
from Sprint_6.locators.main_page_locators import MainPageLocators
import test_data

@pytest.mark.parametrize(
    'num, result',
    [
        (0, test_data.answer_text_0),
        (1, test_data.answer_text_1),
        (2, test_data.answer_text_2),
        (3, test_data.answer_text_3),
        (4, test_data.answer_text_4),
        (5, test_data.answer_text_5),
        (6, test_data.answer_text_6),
        (7, test_data.answer_text_7)
    ]
)
class TestMainPage:
    def test_main_page(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(
            MainPageLocators.QUESTION_ELEMENT,
            MainPageLocators.ANSWER_ELEMENT,
            num
        ) == result


