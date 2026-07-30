from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//header//a[normalize-space()='Личный Кабинет']") #ссылка Личный кабинет

    CONSTRUCTOR_LINK = (By.XPATH, "//header//a[normalize-space()='Конструктор']") #ссылка Конструктор

    STELLAR_BURGERS_LOGO = (By.XPATH, "//header//a[@href='/'][.//*[name()='svg']]")  #логотип

    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")  #кнопка Войти в аккаунт

    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")  #кнопка Оформить заказ после авторизации

    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']") #заголовок конструктора

    NAME_INPUT = (By.XPATH, "//input[@placeholder='Имя']")  #поле Имя

    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email']") #поле Эмэйл

    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']") #поле Пароль

    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']") #кнопка Зарегистрироваться

    LOGIN_LINK_IN_FORM = (By.XPATH, "//a[normalize-space()='Войти']") #Войти в форме

    INVALID_PASSWORD_MESSAGE = (By.XPATH, "//*[contains(normalize-space(), 'Некорректный пароль')]")  #ошибка некорректного пароля

    USER_ALREADY_EXISTS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Такой пользователь уже существует')]") #ошибка уже существующего пользователя

    LOGIN_FORM_TITLE = (By.XPATH, "//h2[normalize-space()='Вход']") #заголовок формы входа

    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")  #кнопка отправки формы входа

    PROFILE_LINK = (By.XPATH, "//a[normalize-space()='Профиль']")  #ссылка Профиль

    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']") #кнопка выхода

    BUNS_TAB = (By.XPATH, "//*[normalize-space()='Булки']/ancestor::*[contains(@class, 'tab')][1]")  #вкладка Булки

    SAUCES_TAB = (By.XPATH, "//*[normalize-space()='Соусы']/ancestor::*[contains(@class, 'tab')][1]")  #вкладка Соусы

    FILLINGS_TAB = (By.XPATH, "//*[normalize-space()='Начинки']/ancestor::*[contains(@class, 'tab')][1]")  #вкладка Начинки

    ACTIVE_BUNS_TAB = (By.XPATH, "//*[normalize-space()='Булки']/ancestor::*[contains(@class, 'tab') and contains(@class, 'current')][1]")  #активная вкладка Булки

    ACTIVE_SAUCES_TAB = (By.XPATH, "//*[normalize-space()='Соусы']/ancestor::*[contains(@class, 'tab') and contains(@class, 'current')][1]")  #активная вкладка Соусы

    ACTIVE_FILLINGS_TAB = (By.XPATH, "//*[normalize-space()='Начинки']/ancestor::*[contains(@class, 'tab') and contains(@class, 'current')][1]")  #активная вкладка Начинки

