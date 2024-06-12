import pytest
from selene import browser, be, have
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


def test_search_pass():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_save_text():
    browser.open('')
    text = "ysertdjsfgjksfgjdfgjdfhksdtk"
    browser.element('[name="q"]').should(be.blank).type('ysertdjsfgjksfgjdfgjdfhksdtk').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу ysertdjsfgjksfgjdfgjdfhksdtk ничего не найдено.'))