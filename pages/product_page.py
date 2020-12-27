from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

from .base_page import BasePage
from .locators import ProductPageLocators

product_name = ""
product_price = ""


class ProductPage(BasePage):

    def open(self):
        self.browser.get(self.url)
        WDW(self.browser, 15) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket")))
        return self

    def product_should_be_in_cart_with_the_same_name_and_the_same_price(self):
        expected_product_added_message = self.product_name + " has been added to your basket."
        actual_product_added_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_product_added_message == actual_product_added_message, \
            "The product added to basket has different name"

        expected_basket_total_message = "Your basket total is now " + self.product_price
        actual_basket_total_message = self.browser.find_element(*ProductPageLocators.CART_TOTAL_MESSAGE).text
        assert expected_basket_total_message == actual_basket_total_message, \
            "The product added to basket has different price"

    def remember_product_name_and_price_and_add_product_to_cart(self):
        # Sets values to global variables 'product_name' and 'product_price'
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_basket_button.click()
        return self

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is present, though it shouldn't"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is present, though it shouldn't"

    def should_be_able_to_go_to_login_page(self):
        self.go_to_login_page()
        assert "login" in self.browser.current_url, "Wrong URL - do not contains 'login'"
