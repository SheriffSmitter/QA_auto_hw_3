import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = 'https://google.com/'
    browser.config.timeout = 10
    browser.config.driver_name = 'firefox'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.window_height = 1080
    browser.config.window_width = 1920
