from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


os.environ['PATH'] += r";C:/Program Files (x86)/"
driver = webdriver.Chrome()

def login_test(id, key):
    driver.get("https://cfportal.ktm.yetiappcloud.com/auth/login")
    driver.implicitly_wait(5)
    email = driver.find_element(By.XPATH, '//input[@name="username"]')
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    button = driver.find_element(By.XPATH, '//button[@class="MuiLoadingButton-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-fullWidth MuiButtonBase-root css-wmpqfy"]')

    email.send_keys(id)
    password.send_keys(key)
    button.click()
    time.sleep(3)
    if driver.current_url == "https://cfportal.ktm.yetiappcloud.com/dashboard/app":
        print("success")


login_test("sonzay9+reporter@gmail.com","Test12345_")