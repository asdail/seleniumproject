from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class All_pages:
    def __init__(self,driver):
        self.driver = driver

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

    def cart_hovering(self):
        element_to_hover_over = self.driver.find_element_by_id("menuCart")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        return hover.perform()

    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//*[@id=toolTipCart]/div/table/tfoot/tr[1]/td[2]/span").text

    def name_of_the_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/h3").text

    def color_of_the_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/label/span").text

    def qty_per_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/label").text

    def price_per_item(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[3]/p").text

    def remove_item_from_cart(self,number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[3]/div").click()

    def total_items_in_cart(self):
        return self.driver.find_element_by_xpath('/html/body/header/nav/ul/li[2]/ul/li/tool-tip-cart/div/table/tfoot/tr[1]/td[1]/span/label').text

    def checkout(self):
        return self.driver.find_element_by_id("checkOutPopUp").click()


