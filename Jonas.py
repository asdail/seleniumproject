import unittest
from selenium import webdriver
from Tablets import Tablets
from main_page import Main_page
from Cart_pop_up import Cart_pop_up
from CheckOut import Checkout
from HP_ElitePad import hp_ElitePad
from HP_PRO import HP_pro
from HP_ELITE_X2 import HP_elite_x2
from Cart import Cart
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AOS (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Selenium\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get('https://advantageonlineshopping.com/#/')
        print('setUp')

    def tearDown(self):
        self.driver.close()
        print('tearDown')

    def part_6(self):
        self.driver = Main_page(self.driver)
        self.driver.tablets()
        self.driver = Tablets(self.driver)
        self.driver.hp_eletepad()
        self.driver = hp_ElitePad(self.driver)
        self.driver.add_to_cart()
        self.driver.tablets()
        self.driver = Tablets(self.driver)
        self.driver.hp_elite()
        self.driver = HP_elite_x2(self.driver)
        self.driver.add_to_cart()
        self.driver = Cart_pop_up(self.driver)
        self.driver.cart()
        self.driver = Cart(self.driver)
        self.driver.edit_cart('1')
        self.driver = hp_ElitePad(self.driver)
        self.driver.quantity('2')
        self.driver.cart()
        self.driver = Cart(self.driver)
        self.driver.edit_cart('2')
        self.driver = HP_elite_x2(self.driver)
        self.driver.quantity('2')
        self.driver = Cart_pop_up(self.driver)
        self.driver.cart()
        self.driver = Cart(self.driver)
        self.assertEqual(self.driver.qty_per_item('1'), '2')
        self.assertEqual(self.driver.qty_per_item('2'), '2')