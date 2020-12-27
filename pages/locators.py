from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class CartPageLocators():
    CART_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    CART_ITEM = (By.CLASS_NAME, "basket-items")
    CART_SEARCH_BUTTON = (By.CSS_SELECTOR, ".form-group > input")
    CART_TITLE = (By.CSS_SELECTOR, ".action > h1")


class LoginPageLocators():
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > .btn-primary")
    LOGIN_FORM = (By.ID, "login_form")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REGISTER_FORM = (By.ID, "register_form")


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    MAIN_PAGE_SEARCH_BUTTON = (By.CSS_SELECTOR, ".form-group > input")
    OTHER_GOOD_BOOKS_ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-block")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    CART_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(3) > .alertinner > :first-child")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :first-child > .alertinner")
