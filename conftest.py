import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = 'https://google.com/'
    browser.config.driver_name = 'firefox'
    driver_options = webdriver.FirefoxOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()
