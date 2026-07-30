from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestData, Urls
from helpers import ( click, fill_registration_form, generate_user, register_unique_user, wait_visible)
from locators import Locators


class TestRegistration:
    def test_successful_registration(self, driver):
        user = register_unique_user(driver)

        assert user["name"] != ""
        assert user["email"].startswith("liza_shishlo_50_")
        assert user["email"].endswith("@yandex.ru")
        assert len(user["password"]) >= 6

        assert "/login" in driver.current_url
        assert wait_visible(driver, Locators.LOGIN_FORM_TITLE).is_displayed()


    def test_registration_with_short_password_shows_error(self, driver):
        user = generate_user()
        user["password"] = TestData.INVALID_PASSWORD

        driver.get(Urls.REGISTER_URL)
        fill_registration_form(driver, user)
        click(driver, Locators.REGISTER_BUTTON)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD_MESSAGE))
        assert (TestData.INVALID_PASSWORD_ERROR in error_message.text)
        assert "/register" in driver.current_url

