import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_existence(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector('.btn-add-to-basket')
    time.sleep(5)
