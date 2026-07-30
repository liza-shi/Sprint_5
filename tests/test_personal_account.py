from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import Urls
from helpers import ( click, open_personal_account, register_and_login, wait_visible)
from locators import Locators


class TestPersonalAccount:
    def assert_constructor_opened(self, driver):
        WebDriverWait(driver, 10).until(lambda current_driver: current_driver.current_url.rstrip("/") == Urls.BASE_URL.rstrip("/"))

        assert wait_visible(driver, Locators.CONSTRUCTOR_TITLE).is_displayed()


    def test_open_personal_account_by_header_link(self, driver):
        register_and_login(driver)
        open_personal_account(driver)

        assert ("/profile" in driver.current_url or "/account" in driver.current_url)
        assert wait_visible(driver, Locators.PROFILE_LINK).is_displayed()


    def test_go_from_personal_account_to_constructor_by_link(self, driver):
        register_and_login(driver)
        open_personal_account(driver)
        click(driver, Locators.CONSTRUCTOR_LINK)
        self.assert_constructor_opened(driver)


    def test_go_from_personal_account_to_constructor_by_logo(self, driver):
        register_and_login(driver)
        open_personal_account(driver)
        click(driver, Locators.STELLAR_BURGERS_LOGO)
        self.assert_constructor_opened(driver)


    def test_logout_from_personal_account(self, driver):
        register_and_login(driver)
        open_personal_account(driver)
        click(driver, Locators.LOGOUT_BUTTON)
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))

        assert "/login" in driver.current_url
        assert wait_visible(driver, Locators.LOGIN_FORM_TITLE).is_displayed()