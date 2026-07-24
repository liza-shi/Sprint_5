class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    LOGIN_URL = f"{BASE_URL}/login"
    REGISTER_URL = f"{BASE_URL}/register"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"


class TestData:
    USER_NAME = "Елизавета"
    INVALID_PASSWORD = "12345"
    INVALID_PASSWORD_ERROR = "Некорректный пароль" 