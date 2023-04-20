import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')) > 0