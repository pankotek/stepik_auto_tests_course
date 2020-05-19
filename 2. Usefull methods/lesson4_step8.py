import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('solve').click()


finally:
    pass
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

