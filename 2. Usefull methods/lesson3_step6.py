import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name('button').click()
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input_line = browser.find_element_by_xpath("//input[@type='text']")
    input_line.send_keys(y)
    browser.find_element_by_tag_name('button').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
