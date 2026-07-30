from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestData, Urls
from generators import generate_login, generate_password
from locators import Locators


DEFAULT_TIMEOUT = 15


def wait_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def click(driver, locator, timeout=DEFAULT_TIMEOUT):
    element = wait_clickable(driver, locator, timeout)
    element.click()


def generate_user():
    return {"name": TestData.USER_NAME, "email": generate_login(), "password": generate_password()}


def fill_registration_form(driver, user):
    wait_visible(driver, Locators.NAME_INPUT).send_keys(user["name"])
    wait_visible(driver, Locators.EMAIL_INPUT).send_keys(user["email"])
    wait_visible(driver, Locators.PASSWORD_INPUT).send_keys(user["password"])


def fill_login_form(driver, user):
    email_input = wait_visible(driver, Locators.EMAIL_INPUT)
    email_input.clear()
    email_input.send_keys(user["email"])

    password_input = wait_visible(driver, Locators.PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys(user["password"])


def register_unique_user(driver, attempts=15):
    for _ in range(attempts):
        user = generate_user()
        driver.get(Urls.REGISTER_URL)
        fill_registration_form(driver, user)
        click(driver, Locators.REGISTER_BUTTON)

        try:
            WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_contains("/login"))
            wait_visible(driver, Locators.LOGIN_FORM_TITLE)

            return user

        except TimeoutException:
            user_exists = driver.find_elements(*Locators.USER_ALREADY_EXISTS_MESSAGE)
            if user_exists:
                continue
            raise

    raise AssertionError("Не удалось зарегистрировать пользователя: ""сгенерированные email уже заняты")


def login_from_open_form(driver, user):
    fill_login_form(driver, user)

    click(driver, Locators.LOGIN_BUTTON)
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(lambda current_driver: current_driver.current_url.rstrip("/") == Urls.BASE_URL.rstrip("/"))
    wait_visible(driver, Locators.ORDER_BUTTON)


def register_and_login(driver):
    user = register_unique_user(driver)

    login_from_open_form(driver, user)
    return user


def open_personal_account(driver):
    click(driver, Locators.PERSONAL_ACCOUNT_LINK)
    wait_visible(driver, Locators.PROFILE_LINK)
    