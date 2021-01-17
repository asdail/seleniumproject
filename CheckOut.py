from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout:
    def __init__(self,driver):
        self.driver = driver

    #Check that you are in the right place = order payment
    def navigation_line(self):
        return self.driver.find_element_by_css_selector("a[translate = ORDER_PAYMENT]").text()

    def edit_shipping_details(self):
        return self.driver.find_element_by_css_selector("a[translate = Edit_shipping_Details]").click()

    def new_account(self):
        return self.driver.find_element_by_id("registration_btnundefined").click()

    def username(self, input):
        return self.driver.find_element_by_name("usernameInOrderPayment").send_keys(input)

    def password(self, input):
        return self.driver.find_element_by_name("passwordInOrderPayment").send_keys(input)

    def login(self):
        return self.driver.find_element_by_id("login_btnundefined").click()

    # edit path
    def next_page(self):
        return self.driver.find_element_by_css_selector("button[id=next_btn]").click()

    def payment_method_safepay(self):
        return self.driver.find_element_by_css_selector("img[alt=Safepay]").click()

    def safepay_username(self, text):
        self.driver.find_element_by_css_selector("input[name=safepay_username]").click
        self.driver.find_element_by_css_selector("input[name=safepay_username]").send_keys(text)

    def safepay_password(self, text):
        self.driver.find_element_by_css_selector("input[name=safepay_password]").click
        self.driver.find_element_by_css_selector("input[name=safepay_password]").send_keys(text)

    def pay_now(self):
        return self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

    def order_succeed(self):
        return self.driver.find_element_by_css_selector("span[translate=Thank_you_for_buying_with_Advantage]").text()

    def checkout(self):
        return self.driver.find_element_by_id("checkOutPopUp").click()

