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

cookies = browser.get_cookies()
print("Cookies type: ")
print(type(cookies))
print("First cookie type: ")
print(type(cookies[0]))
print("Cookies length: ")
print(len(cookies))
print("Cookies value: ")
print(cookies)
print('Cookie: NID=')
print(browser.get_cookie('NID'))

sleep(2)
browser.quit()
