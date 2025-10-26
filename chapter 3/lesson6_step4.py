import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """Фикстура для инициализации браузера"""
    driver = webdriver.Chrome()  # настройка ДО теста
    yield driver  
    driver.quit()  # очистка ПОСЛЕ теста


class TestLogin:
    def test_authorization(self, load_config, browser):  # ← добавляем browser как параметр
        # Создаем явное ожидание
        wait = WebDriverWait(browser, 10)  # ← используем browser вместо self.browser
        
        # Получаем логин и пароль из конфига
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        
        # Открываем страницу урока
        browser.get("https://stepik.org/lesson/236895/step/1")  # ← browser вместо self.browser
        
        # Нажимаем кнопку "Войти" 
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "ember483"))
        )
        login_button.click()
        
        # Заполняем форму авторизации
        email_input = wait.until(
            EC.visibility_of_element_located((By.ID, "id_login_email"))
        )
        email_input.send_keys(login)
        
        password_input = browser.find_element(By.ID, "id_login_password")  # ← browser
        password_input.send_keys(password)
        
        # Нажимаем кнопку "Войти" в форме
        submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")  # ← browser
        submit_button.click()
        
        # Ждем исчезновения поп-апа авторизации 
        wait.until(
            EC.invisibility_of_element_located((By.ID, "ember581"))
        )
        
        # Ждем появления аватара пользователя
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "navbar__profile-img"))
        )
        
        print("Авторизация прошла успешно!")