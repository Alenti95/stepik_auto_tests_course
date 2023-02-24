from selenium.webdriver.common.by import By

def test_find_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert len(browser.find_elements(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')) > 0, 'basket button not found'
