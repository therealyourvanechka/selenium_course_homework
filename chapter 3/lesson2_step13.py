import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

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
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Registration failed for registration1.html")
    
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

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
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Registration failed for registration2.html")


if __name__ == "__main__":
    unittest.main()