from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page:
    def __init__(self,driver):
        self.driver = driver
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > header >nav >div  >a")))


    def user(self):
        return self.driver.find_element_by_id("menuUserSVGPath").click()

    def user_my_account(self):
        return self.driver.find_element_by_css_selector("label[translate=My_account]").click()


    def user_my_orders(self):
        return self.driver.find_element_by_css_selector("label[translate=My_Orders]").click()

    def user_sigh_out(self):
        return self.driver.find_element_by_css_selector("label[translate=Sign_out]").click()

    def cart(self):
        return self.driver.find_element_by_id("menuCart").click()

    def back_to_main(self):
        return self.driver.find_element_by_css_selector("div[class=logo]").click()

    def speakers(self):
        return self.driver.find_element_by_id("speakersImg").click()

    def tablets(self):
        return self.driver.find_element_by_id("tabletsImg").click()

    def laptops(self):
        return self.driver.find_element_by_id("laptopsImg").click()

    def mice(self):
        return self.driver.find_element_by_id("miceImg").click()

    def headphones(self):
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


