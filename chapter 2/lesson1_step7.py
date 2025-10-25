from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение x
    image = browser.find_element(By.ID, "treasure") 
    x = image.get_attribute("valuex")
    y = calc(x)

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
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    
finally:
    # Даем время для копирования результата
    time.sleep(30)
    # Закрываем браузер
    browser.quit()