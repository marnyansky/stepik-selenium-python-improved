from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):

    def cart_should_be_empty(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEM), \
            "There is at least one item in the basket"
        assert "empty" in self.browser.find_element(*CartPageLocators.BASKET_IS_EMPTY_MESSAGE).text, \
            "The message informing that the basket is empty is not displayed"
