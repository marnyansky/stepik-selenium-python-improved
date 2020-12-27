from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):

    def cart_should_be_empty(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), \
            "There is at least one item in the basket"
        assert "empty" in self.browser.find_element(*CartPageLocators.CART_IS_EMPTY_MESSAGE).text, \
            "The message informing that the basket is empty is not displayed"

    def open(self):
        self.browser.get(self.url)
        WDW(self.browser, 15)\
            .until(EC.visibility_of((By.CSS_SELECTOR, ".action > h1")))
        WDW(self.browser, 15)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-group > input")))
        return self
