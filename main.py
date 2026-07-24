from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    print("Заголовок страницы:", driver.title)

    text_box = driver.find_element(By.NAME, "my-text")

    text_box.send_keys("Привет, Selenium!")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button")
    submit_button.click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    print("Результат:", message.text)

    input("Нажми Enter в терминале, чтобы закрыть браузер...")

finally:
    driver.quit()