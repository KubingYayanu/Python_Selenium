from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def find_element(browser, by=By.ID, value=None, time_to_wait=10) -> WebElement:
    wait = WebDriverWait(browser, time_to_wait)
    return wait.until(EC.presence_of_element_located((by, value)))

browser = webdriver.Chrome()
browser.maximize_window()

browser.implicitly_wait(10)
browser.get("https://www.google.com/")

search_box = find_element(browser, By.CSS_SELECTOR, "#APjFqb")
search_box.clear()
search_box.send_keys("youtube")

sleep(2)

print("Property: id=" + search_box.get_property('id'))
print("Attribute: value=" + search_box.get_attribute('value'))

gmail = find_element(browser, By.CSS_SELECTOR, "#gb > div > div:nth-child(1) > div > div:nth-child(1) > a")
print("Text: text=" + gmail.text)

sleep(2)
browser.quit()