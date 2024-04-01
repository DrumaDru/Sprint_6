from Sprint_6.pages.base_page import BasePage


class MainPage(BasePage):

    def get_answer_text(self, locator_q, locator_a, num):
        question_element_formatted = self.format_locators(locator_q, num)
        answer_element_formatted = self.format_locators(locator_a, num)
        self.scroll_into_view_element(question_element_formatted)
        self.click_to_element(question_element_formatted)
        return self.get_text_from_element(answer_element_formatted)

    def get_dzen(self, locator_y, locator_dz):
        self.click_to_element(locator_y)
        self.find_element_with_wait(locator_dz)
