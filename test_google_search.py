import pytest
from selene import browser, be, have


def test_search_pass():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_save_text():
    browser.open('')
    text = "ysertdjsfgjksfgjdfgjdfhksdtk"
    browser.element('[name="q"]').should(be.blank).type('ysertdjsfgjksfgjdfgjdfhksdtk').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу ysertdjsfgjksfgjdfgjdfhksdtk ничего не найдено.'))