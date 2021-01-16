import unittest
from selenium import webdriver
from Locators import Locators
from Tablets import Tablets
from main_page import Main_page
from All_pages import All_pages
from CheckOut import Checkout
from HP_ElitePad import hp_ElitePad
from HP_PRO import HP_pro
from HP_ELITE_X2 import HP_elite_x2
from Cart import Cart
from Create_an_account import Create_an_account
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AOS (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Selenium\chromedriver.exe')
        self.mainpage = Main_page(self.driver)
        self.tablets = Tablets(self.driver)
        self.hp_elitepad = hp_ElitePad(self.driver)
        self.hp_elite = HP_elite_x2(self.driver)
        self.general = All_pages(self.driver)
        self.cart = Cart(self.driver)

        self.driver.implicitly_wait(10)
        self.driver.get('https://advantageonlineshopping.com/#/')
        self.driver.maximize_window()
        print('setUp')

    def tearDown(self):
        self.driver = webdriver.Chrome(executable_path='C:\Selenium\chromedriver.exe')
        self.driver.close()
        print('tearDown')

    def test_part_6(self):
        self.mainpage.tablets()
        self.tablets.home().send_keys(Keys.PAGE_DOWN)
        self.tablets.hp_elitepad()
        self.hp_elitepad.add_to_cart()
        self.hp_elitepad.tablets()
        self.tablets.hp_elite()
        self.hp_elite.add_to_cart()
        self.general.cart()
        time.sleep(7.0)
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/article/div[1]/table/tbody/tr[1]/td[6]/span/a[1]")))
        self.cart.edit_cart("1")
        self.hp_elite.quantity("2")
        self.hp_elite.add_to_cart()
        self.general.cart()
        self.cart.edit_cart("2")
        self.hp_elitepad.quantity("2")
        self.hp_elitepad.add_to_cart()
        self.general.cart()
        time.sleep(7.0)
        self.assertEqual(self.cart.qty_per_item('1'), '2')
        self.assertEqual(self.cart.qty_per_item('2'), '2')
        self.general.back_to_main()

    def test_part_7(self):
        self.mainpage.tablets()
        self.tablets.hp_elitepad()
        self.hp_elitepad.add_to_cart()
        self.hp_elitepad.tablets()
        self.assertEqual(self.driver.find_element_by_xpath("/html/body/div[3]/section/article/div[2]").text ,"HOME TABLETS")
        self.general.back_to_main()
        self.assertEqual(self.driver.current_url, "https://advantageonlineshopping.com/#/")

    def test_part_8(self):
        pass