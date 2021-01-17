from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Create_an_account:

    def __init__(self, driver):
        self.driver = driver

    def general(self):
        return self.driver.find_element_by_css_selector("body")

    def username(self, input):
        return self.driver.find_element_by_name("usernameRegisterPage").send_keys(input)

    def email(self, input):
        return self.driver.find_element_by_name("emailRegisterPage").send_keys(input)

    def password(self, input):
        return self.driver.find_element_by_name("passwordRegisterPage").send_keys(input)

    def confirm_password(self, input):
        return self.driver.find_element_by_name("confirm_passwordRegisterPage").send_keys(input)

    def terms(self):
        return self.driver.find_element_by_name("i_agree").click()

    def register(self):
        return self.driver.find_element_by_id("register_btnundefined").click()


