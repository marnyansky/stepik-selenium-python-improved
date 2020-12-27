import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()\
            .go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page_with_forms()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()\
            .should_be_login_link()
