from .base_page import BasePage


class MainPage(BasePage):

    # send given arguments to superclass
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
