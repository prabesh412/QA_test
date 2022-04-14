from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import user.constants as const
import time

class login(webdriver.Chrome):
    def __init__(self, driver_path=r";C:/Program Files (x86)/", teardown=False):
        self.teardown=teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(login,self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def first_page(self):
        self.get(const.base_url+'dashboard/app')



    def login_test(self, id, key):
        self.get("https://cfportal.ktm.yetiappcloud.com/auth/login")
        self.implicitly_wait(5)
        email = self.find_element(By.XPATH, '//input[@name="username"]')
        password = self.find_element(By.XPATH, '//input[@name="password"]')
        button = self.find_element(By.XPATH,'//button[@class="MuiLoadingButton-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-fullWidth MuiButtonBase-root css-wmpqfy"]')

        email.send_keys(id)
        password.send_keys(key)
        button.click()
        time.sleep(3)
        if self.current_url == "https://cfportal.ktm.yetiappcloud.com/dashboard/app":
            print("success")
            add_species(self, 'https://cfportal.ktm.yetiappcloud.com/dashboard/species')

    def incorrect_logintest(self, id, key):
        self.get("https://cfportal.ktm.yetiappcloud.com/auth/login")
        self.implicitly_wait(5)
        email = self.find_element(By.XPATH, '//input[@name="username"]')
        password = self.find_element(By.XPATH, '//input[@name="password"]')
        button = self.find_element(By.XPATH,'//button[@class="MuiLoadingButton-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-fullWidth MuiButtonBase-root css-wmpqfy"]')

        email.send_keys(id)
        password.send_keys(key)
        button.click()
        time.sleep(3)
        response = self.find_element(By.XPATH, '//div[@class="MuiAlert-message css-s6w8ns"]').text
        if response == "Invalid Credentials.":
            print("success")

    def signup_test(self):
        self.get("https://cfportal.ktm.yetiappcloud.com/auth/register")
        msg = self.find_element(By.XPATH, '//p[@class="MuiTypography-root MuiTypography-h3 MuiTypography-paragraph css-zoxu81"]').text
        if msg == "Coming Soon!":
            print("Failed")
        else:
            print("working on it")


    def footer_test(self):
        self.get('https://cfportal.ktm.yetiappcloud.com/partners')
        self.implicitly_wait(5)
        link = self.find_element(By.XPATH, '//div[@class="css-ikzlcq"][1]/a[@href="/about-us"]').click()
        if self.current_url == "https://cfportal.ktm.yetiappcloud.com/404":
            print("success")

    def sign_up_button(self):
        self.get('https://cfportal.ktm.yetiappcloud.com/')
        self.implicitly_wait(5)
        resp = self.find_element(By.XPATH, '//div[@style="opacity: 1; transform: none;"]/a[@class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButtonBase-root  css-1fayv3"]').click()
        if self.current_url == "https://cfportal.ktm.yetiappcloud.com/dashboard":
            print("sucess")