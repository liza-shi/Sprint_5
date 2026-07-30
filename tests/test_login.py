from data import Urls
from helpers import (click, login_from_open_form, register_unique_user, wait_visible)
from locators import Locators



class TestLogin:
    def test_login_by_login_account_button_on_main_page(self, driver):
        user = register_unique_user(driver)
        driver.get(Urls.BASE_URL)
        click(driver, Locators.LOGIN_ACCOUNT_BUTTON)
        login_from_open_form(driver, user)

        assert (driver.current_url.rstrip("/") == Urls.BASE_URL.rstrip("/"))
        assert wait_visible(driver, Locators.ORDER_BUTTON).is_displayed()


    def test_login_by_personal_account_link(self, driver):
        user = register_unique_user(driver)
        driver.get(Urls.BASE_URL)
        click(driver, Locators.PERSONAL_ACCOUNT_LINK)
        login_from_open_form(driver, user)

        assert (driver.current_url.rstrip("/") == Urls.BASE_URL.rstrip("/"))
        assert wait_visible( driver, Locators.ORDER_BUTTON).is_displayed()


    def test_login_by_link_in_registration_form(self, driver):
        user = register_unique_user(driver)
        driver.get(Urls.REGISTER_URL)
        click(driver, Locators.LOGIN_LINK_IN_FORM)
        login_from_open_form(driver, user)

        assert (driver.current_url.rstrip("/") == Urls.BASE_URL.rstrip("/"))
        assert wait_visible(driver, Locators.ORDER_BUTTON).is_displayed()


    def test_login_by_link_in_password_recovery_form(self, driver):
        user = register_unique_user(driver)
        driver.get(Urls.FORGOT_PASSWORD_URL)
        click(driver, Locators.LOGIN_LINK_IN_FORM)
        login_from_open_form(driver, user)

        assert (driver.current_url.rstrip("/") == Urls.BASE_URL.rstrip("/"))
        assert wait_visible(driver, Locators.ORDER_BUTTON).is_displayed()
