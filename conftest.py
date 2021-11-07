import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    print(f'params: {user_language=}')

    options = webdriver.ChromeOptions()
    options.add_argument(f'lang={user_language}')
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(5)

    yield browser
    browser.quit()
