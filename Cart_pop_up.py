from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_pop_up:
    def __init__(self,driver):
        self.driver = driver

    def total_items_in_cart(self):
        return self.driver.find_element_by_css_selector("tfoot > tr > td > span > label").text()

    # edit path
    def cart(self):
        return self.driver.find_element_by_id('menuCart').click()

    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//*[@id=toolTipCart]/div/table/tfoot/tr[1]/td[2]/span").text()

    def name_of_the_item(self):
        return self.driver.find_element_by_id("speakersImg").text()

    def color_of_the_item(self):
        return self.driver.find_element_by_css_selector("a > label > span[class=ng-binding]").text()

    def qty_per_item(self):
        return self.driver.find_element_by_xpath("//tr[@id='product']/td[2]/a/label[1]").text()

    def price_per_item(self):
        return self.driver.find_element_by_xpath("//tr[@id='product']/td/p").text()

    def remove_item_from_cart(self):
        return self.driver.find_element_by_xpath("//tr[@id='product']/td/div/div").click()

    def checkout(self):
        return self.driver.find_element_by_id("checkOutPopUp").click()



