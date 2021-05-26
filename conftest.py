import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store', default='en-gb', help='Choose shop language'
    )


@pytest.fixture(scope='function')
def driver(request):
    __chrome_options = ChromeOptions()
    __chrome_options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption('language')})
    driver = webdriver.Chrome(options=__chrome_options)

    yield driver

    driver.quit()
