from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

#General class for object that display in all the site
class All_pages:
    def __init__(self,driver):
        self.driver = driver

# General wait for this page by general element in the page
    def wait(self):
        self.wait = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > header >nav >div  >a")))

# Click on the user icon
    def user(self):
        return self.driver.find_element_by_id("menuUserSVGPath").click()

# click on my account in user
    def user_my_account(self):
        return self.driver.find_element_by_css_selector("label[translate=My_account]").click()

# Click on my orders in user
    def user_my_orders(self):
        return self.driver.find_element_by_css_selector("label[translate=My_Orders]").click()

# click on my orders in user
    def user_sigh_out(self):
        return self.driver.find_element_by_css_selector("label[translate=Sign_out]").click()

# Click on my cart icon
    def cart(self):
        return self.driver.find_element_by_id("menuCart").click()

# Click on the LOGO and back to the main page
    def back_to_main(self):
        return self.driver.find_element_by_css_selector("div[class=logo]").click()

# Do hovering on the cart icon
    def cart_hovering(self):
        element_to_hover_over = self.driver.find_element_by_id("menuCart")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        return hover.perform()

# Display total for payment I have to pay
    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//*[@id=toolTipCart]/div/table/tfoot/tr[1]/td[2]/span").text

# Display the name of the item in cart by index for instance if I want the I product index = 1
    def name_of_the_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/h3").text

# Display the color of the item in cart by index for instance if I want the I product index = 1
    def color_of_the_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/label/span").text

# Display the qty of the item in cart by index for instance if I want the I product index = 1
    def qty_per_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/label[1]").text

# Display the price of the item in cart by index for instance if I want the I product index = 1
    def price_per_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[3]/p").text

# Remove 1 item from the cart by index for instance if I want the I product index = 1
    def remove_item_from_cart(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[3]/div/div").click()

# Display total products I have in my cart
    def total_items_in_cart(self):
        return self.driver.find_element_by_xpath('/html/body/header/nav/ul/li[2]/ul/li/tool-tip-cart/div/table/tfoot/tr[1]/td[1]/span/label').text

# Click on the checkout button
    def checkout(self):
        return self.driver.find_element_by_id("checkOutPopUp").click()

# Function that take string and back the string "clean" with only the numbers for a more accurate test
    def only_numbers(self,string_1):
        nums = ("0123456789")
        only_nums = ""
        for i in range(len(string_1)):
            if string_1[i] in nums:
                only_nums += string_1[i]
        return only_nums



