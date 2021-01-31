from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Class for checkout page
class Checkout:
    def __init__(self,driver):
        self.driver = driver

#Check that you are in the right place = order payment
    def navigation_line(self):
        return self.driver.find_element_by_css_selector("a[translate = ORDER_PAYMENT]").text()

# Click edit shipping details
    def edit_shipping_details(self):
        return self.driver.find_element_by_css_selector("a[translate = Edit_shipping_Details]").click()

# Click "new account"
    def new_account(self):
        return self.driver.find_element_by_id("registration_btnundefined").click()

# Input for username field
    def username(self, input):
        return self.driver.find_element_by_name("usernameInOrderPayment").send_keys(input)

# Input for password field
    def password(self, input):
        return self.driver.find_element_by_name("passwordInOrderPayment").send_keys(input)

#Click log in
    def login(self):
        return self.driver.find_element_by_id("login_btnundefined").click()

# Click next page
    def next_page(self):
        return self.driver.find_element_by_css_selector("button[id=next_btn]").click()

# Click "safepay"
    def payment_method_safepay(self):
        return self.driver.find_element_by_css_selector("img[alt=Safepay]").click()

# Click "mastercredit"
    def payment_method_mastercredit(self):
        return self.driver.find_element_by_name("masterCredit").click()

# Click safepay user name field and enter user name
    def safepay_username(self, text):
        self.driver.find_element_by_css_selector("input[name=safepay_username]").click
        self.driver.find_element_by_css_selector("input[name=safepay_username]").send_keys(text)

# Click safepay password field and enter user name
    def safepay_password(self, text):
        self.driver.find_element_by_css_selector("input[name=safepay_password]").click
        self.driver.find_element_by_css_selector("input[name=safepay_password]").send_keys(text)

# send input - card number
    def card_number(self, input):
        return self.driver.find_element_by_id("creditCard").send_keys(input)

# send input - cvv number
    def cvv_number(self, input):
        return self.driver.find_element_by_name("cvv_number").send_keys(input)

# send input - name of card holder
    def cardholder_name(self, input):
        return self.driver.find_element_by_name("cardholder_name").send_keys(input)

# click pay now
    def pay_now(self):
        return self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

# Click pay now in master credit
    def pay_now_mastercredit(self):
        return self.driver.find_element_by_id("pay_now_btn_ManualPayment").click()

# Display text "order succeed
    def order_succeed(self):
        return self.driver.find_element_by_css_selector("span[translate=Thank_you_for_buying_with_Advantage]").text()

# Click check out
    def checkout(self):
        return self.driver.find_element_by_id("checkOutPopUp").click()

