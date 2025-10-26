import pytest
import math
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def load_config():
    with open('chapter 3/config.json', 'r') as config_file:  
        return json.load(config_file)


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver  
    driver.quit()


class TestStepikMessages:
    @pytest.mark.parametrize('url', [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1", 
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ])
    def test_alien_message(self, browser, load_config, url):
        wait = WebDriverWait(browser, 15)
        
        # Авторизация
        browser.get(url)
        
        login_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login")))
        login_btn.click()
        
        email = wait.until(EC.visibility_of_element_located((By.ID, "id_login_email")))
        email.send_keys(load_config['login_stepik'])
        
        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys(load_config['password_stepik'])
        
        submit_btn = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        submit_btn.click()
        
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "light-tabs")))
        
        # Проверяем состояние текстового поля
        textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        
        # Если поле имеет атрибут disabled (уже заполнено), нажимаем "Решить снова"
        if textarea.get_attribute("disabled"):
            again_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "again-btn.white")))
            again_btn.click()
            # Ждем обновления поля ввода
            textarea = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        
        # Решение задачи
        answer = str(math.log(int(time.time())))
        textarea.clear()
        textarea.send_keys(answer)
        
        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        submit_btn.click()
        
        # Проверка фидбека
        feedback = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        feedback_text = feedback.text.strip()
        
        if feedback_text != "Correct!":
            print(f"🔍 НАЙДЕН КУСОЧЕК: '{feedback_text}'")
        
        assert feedback_text == "Correct!", f"Expected 'Correct!', got '{feedback_text}'"