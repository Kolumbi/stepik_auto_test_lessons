from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip
import time

URL = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return math.log(abs(12 * math.sin(x)))

with webdriver.Chrome() as browser:
    browser.get(URL)

    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.ID, "book").click()

    value = int(browser.find_element(By.ID, "input_value").text)
    value = calc(value)

    browser.find_element(By.ID, "answer").send_keys(str(value))
    browser.find_element(By.ID, "solve").click()

    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split()[-1])
    time.sleep(8)


