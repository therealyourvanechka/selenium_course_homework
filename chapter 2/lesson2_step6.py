from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value") 
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    # Вводим ответ
    input_ans = browser.find_element(By.ID, "answer")
    input_ans.send_keys(y)  # str() не нужен, т.к. calc() уже возвращает строку

    # Отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")  # Исправлена опечатка
    checkbox.click()

    # Выбираем radiobutton
    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()

    # Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # Даем время для копирования результата
    time.sleep(30)
    # Закрываем браузер
    browser.quit()