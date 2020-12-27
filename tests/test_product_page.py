import mimesis  # Faker alternative
import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()\
        .remember_product_name_and_price_and_add_product_to_cart()\
        .solve_quiz_and_get_code()\
        .product_should_be_in_cart_with_the_same_name_and_the_same_price()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()\
        .should_be_able_to_go_to_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()\
        .go_to_cart()
    page = CartPage(browser, browser.current_url)
    page.cart_should_be_empty()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()\
        .go_to_cart()
    page = CartPage(browser, browser.current_url)
    page.cart_should_be_empty()


@pytest.mark.xfail(raises=AssertionError, reason="test should xfail (Stepik.org course > module 4.3.6)")
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()\
        .remember_product_name_and_price_and_add_product_to_cart()\
        .should_not_be_success_message()


@pytest.mark.xfail(raises=AssertionError, reason="test should xfail (Stepik.org course > module 4.3.6)")
def test_guest_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()\
        .remember_product_name_and_price_and_add_product_to_cart()\
        .success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()\
        .should_be_login_link()


class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        reg_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, reg_link)
        page.open()\
            .should_be_register_form()

        f_person = mimesis.Person()
        f_email = f_person.email(domains=['mimesis.name'], unique=True)
        f_password = f_person.password(length=10, hashed=False)
        page.register_new_user(f_email, f_password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()\
            .remember_product_name_and_price_and_add_product_to_cart()\
            .solve_quiz_and_get_code()\
            .product_should_be_in_cart_with_the_same_name_and_the_same_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()\
            .should_not_be_success_message()
