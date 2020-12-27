import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Changes UI language through CLI
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='--lang=en',
                     help='Choose language - default is English (UK)')


@pytest.fixture(scope="function")
def browser(request):
    # Changes UI language using Options instance
    options_set = Options()
    user_language = request.config.getoption("language")
    options_set.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Launches browser with a set of options
    print("\nStarting Chrome browser for testing...")
    browser = webdriver.Chrome(options=options_set)
    yield browser

    # Closes browser
    print("\nQuitting browser...")
    browser.quit()
