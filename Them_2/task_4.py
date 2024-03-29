from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input1.send_keys(y)
    option2 = browser.find_element(By.ID, "robotCheckbox")
    option2.click()
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
