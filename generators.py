import secrets
import string

def generate_login():
    random_number = secrets.randbelow(1000)

    return f"liza_shishlo_50_{random_number:03d}@yandex.ru"

def generate_password(length=10):
    if length < 6:
        raise ValueError("Длина корректного пароля должна быть не меньше 6 символов")

    symbols = string.ascii_letters + string.digits

    return "".join(
        secrets.choice(symbols)
        for _ in range(length))