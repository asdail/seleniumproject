from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tablets:

    def __init__(self, driver):
        self.driver = driver

    def hp_eletepad(self):
        return self.driver.find_element_by_id('16').click()

    def hp_elite(self):
        return self.driver.find_element_by_id('17').click()

    def hp_pro(self):
        return self.driver.find_element_by_id('18').click()

    def home(self):
        return self.driver.find_element_by_link_text('HOME')