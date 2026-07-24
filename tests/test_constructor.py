from data import Urls
from helpers import click, wait_visible
from locators import Locators


def test_buns_tab_works(driver):
    driver.get(Urls.BASE_URL)
    click(driver, Locators.FILLINGS_TAB)
    wait_visible(driver, Locators.ACTIVE_FILLINGS_TAB)
    click(driver, Locators.BUNS_TAB)

    assert wait_visible(driver, Locators.ACTIVE_BUNS_TAB).is_displayed()


def test_sauces_tab_works(driver):
    driver.get(Urls.BASE_URL)
    click(driver, Locators.SAUCES_TAB)

    assert wait_visible(driver, Locators.ACTIVE_SAUCES_TAB).is_displayed()


def test_fillings_tab_works(driver):
    driver.get(Urls.BASE_URL)
    click(driver, Locators.FILLINGS_TAB)

    assert wait_visible(driver, Locators.ACTIVE_FILLINGS_TAB).is_displayed()