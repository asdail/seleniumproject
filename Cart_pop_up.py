from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cart_pop_up:
    def __init__(self,driver):
        self.driver = driver

        driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")

        driver.implicitly_wait(10)

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.maximize_window()

#edit path
    def total_items_in_cart(self):
        return self.driver.find_element_by_xpath("//*[@id=toolTipCart]/div/table/tfoot/tr[1]/td[1]/span/label").text()

    # edit path
    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//*[@id=toolTipCart]/div/table/tfoot/tr[1]/td[2]/span").text()

    def name_of_the_item(self):
        return self.driver.find_element_by_id("speakersImg").click()

    def color_of_the_item(self):
        return self.driver.find_element_by_css_selector("a > label > span[class=ng-binding]").text()

    # product > td:nth-child(2) > a > label:nth-child(3) > span
    def qty_per_item(self):
        return self.driver.find_element_by_id("laptopsImg").click()

    def price_per_item(self):
        return self.driver.find_element_by_id("miceImg").click()

    def remove_item_from_cart(self):
        return self.driver.find_element_by_id("headphonesImg").click()

    def special_offer(self):
        return self.driver.find_element_by_id("see_offer_btn").click()

    def chat_with_us(self):
        return self.driver.find_element_by_id("chatLogo").click()

    def facebook(self):
        return self.driver.find_element_by_css_selector("img[name=follow_facebook]").click()

    def twitter(self):
        return self.driver.find_element_by_css_selector("img[name=follow_twitter]").click()

    def linkedin(self):
        return self.driver.find_element_by_css_selector("img[name=follow_linkedin]").click()
