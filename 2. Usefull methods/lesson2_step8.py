import os
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('Name')
    browser.find_element_by_name('lastname').send_keys('Second Name')
    browser.find_element_by_name('email').send_keys('Email')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)
    browser.find_element_by_tag_name('button').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
