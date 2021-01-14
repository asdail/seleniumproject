from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Tablets:

    def __init__(self, driver):
        self.driver = driver

    def home(self):
            return self.driver.find_element_by_link_text('HOME')

    def hp_eletepad(self):
        return self.driver.find_element_by_id("16").click()

    def hp_elite(self):
        return self.driver.find_element_by_id('17').click()

    def hp_pro(self):
        return self.driver.find_element_by_id('18').click()