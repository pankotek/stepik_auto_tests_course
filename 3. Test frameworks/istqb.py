import pytest
from selenium import webdriver

link = "http://istqb-training.ru/Exam/Start?language=ru&isNative=true"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        for i in range(40):
            browser.find_element_by_css_selector("[name='AnswerRadio']").click()
            imp
            browser.find_element_by_css_selector("#nextQuestButton").click()
