from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

option = find_element(
    browser, By.XPATH, "//*[@id=\"Zrbbw\"]/div[1]/span[contains(., 'music')]"
).click()

sleep(2)
browser.quit()