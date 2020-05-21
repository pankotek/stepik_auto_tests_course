import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_aliens(browser, link):
    browser.get(link)
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
    answer = math.log(int(time.time()))
    browser.find_element_by_tag_name('textarea').send_keys(str(answer))
    browser.find_element_by_tag_name('button').click()
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'pre')))
    message = browser.find_element_by_tag_name('pre').text
    assert message == 'Correct!'
