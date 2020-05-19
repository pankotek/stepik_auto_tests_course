from selenium import webdriver

try:
    def test_abs1():
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
        first_name.send_keys('Name')
        last_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
        last_name.send_keys('Surname')
        email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
        email.send_keys('Email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == "Congratulations! You have successfully registered!"


    def test_abs2():
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
        first_name.send_keys('Name')
        last_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
        last_name.send_keys('Surname')
        email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
        email.send_keys('Email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == "Congratulations! You have successfully registered!"
finally:
    webdriver.Chrome.quit()
