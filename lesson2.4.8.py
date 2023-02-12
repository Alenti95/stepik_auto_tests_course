from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[id="price"]'), '$100'))
    button = browser.find_element(By.CSS_SELECTOR, '[onclick="checkPrice();"]')
    button.click()
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    input1 = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
    input1.send_keys(calc(x))
    browser.execute_script('window.scroll(0, 100);')
    button2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(20)
    browser.quit()
    