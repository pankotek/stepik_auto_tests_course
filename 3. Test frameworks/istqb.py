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
    def test_autocomplete(self, browser):
        browser.get(link)
        for i in range(40):
            random.choice(browser.find_elements_by_name('AnswerRadio')).click()
            browser.find_element_by_id("nextQuestButton").click()
        browser.find_element_by_css_selector('#endExam').click()
        time.sleep(10)
