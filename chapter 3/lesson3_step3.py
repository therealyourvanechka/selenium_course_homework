import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration:
    
    @pytest.fixture(autouse=True)
    def browser_setup(self):
        self.browser = webdriver.Chrome() # настройка ДО теста
        yield  # пауза, тест работает с браузером
        self.browser.quit() # очистка ПОСЛЕ теста
    
    @pytest.mark.parametrize("url", [
        "http://suninjuly.github.io/registration1.html",
        "http://suninjuly.github.io/registration2.html"
    ])
    def test_registration(self, url):
        self.browser.get(url)

        # Заполняем обязательные поля
        input_first_name = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input_first_name.send_keys("Ivan")

        input_last_name = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input_last_name.send_keys("Petrov")

        input_email = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input_email.send_keys("email@mail.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        time.sleep(1)

        # Проверяем успешность регистрации
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        assert welcome_text == "Congratulations! You have successfully registered!", \
            f"Registration failed for {url}. Got: {welcome_text}"