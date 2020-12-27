from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

from .base_page import BasePage


class MainPage(BasePage):

    # send given arguments to superclass
    # def __init__(self, *args, **kwargs):
    # super(MainPage, self).__init__(*args, **kwargs)

    def open(self):
        self.browser.get(self.url)
        WDW(self.browser, 15) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-group > input")))
        WDW(self.browser, 15) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-block")))
        return self
