import pytest
from selenium import webdriver
import time
import random

link = "http://istqb-training.ru/Exam/Start?language=ru&isNative=true"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        for i in range(40):
            random.choice(browser.find_elements_by_name('AnswerRadio')).click()
#            time.sleep(0.5)
            browser.find_element_by_id("nextQuestButton").click()
#            time.sleep(0.5)
        browser.find_element_by_css_selector('#endExam').click()
        time.sleep(10)
