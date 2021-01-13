from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class checkout:
    def __init__(self,driver):
        self.driver = driver

#Check that you are in the right place = order payment
    def navigation_line(self):
        return self.driver.find_element_by_css_selector("a[translate = MY_ORDERS]").text()


    def order_number(self):
        return self.driver.find_element_by_xpath("//div[@id=myAccountContainer]/div/div/div[2]/div[1]/div[1]/label").text()

    def order_date(self):
        return self.driver.find_element_by_xpath("//div[@id=myAccountContainer]/div/div/div[2]/div[1]/div[2]/label").text()

    def total_price(self):
        return self.driver.find_element_by_xpath("//div[@id=myAccountContainer]/div/div/div[2]/div[1]/div[3]/label").text()

