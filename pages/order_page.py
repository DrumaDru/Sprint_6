from Sprint_6.pages.base_page import BasePage


class OrderPage(BasePage):

    def scooter_button(self, locator_o, locator_s, locator_t):
        self.click_to_element(locator_o)
        self.click_to_element(locator_s)
        return self.get_text_from_element(locator_t)




