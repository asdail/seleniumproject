import unittest
from Tablets import *
from main_page import *
from HP_ElitePad import *
from HP_PRO import *
from Cart_pop_up import *

class AOSProject(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")

        self.driver.implicitly_wait(10)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()

    def add_two_products(self):
        main_page.tablets()
        Tablets.hp_eletepad()
        hp_ElitePad.color_black()
        hp_ElitePad.quantity("2")
        hp_ElitePad.add_to_cart()
        main_page.back_to_main()

        main_page.tablets()
        Tablets.hp_pro()
        hp_pro.color_gray()
        hp_pro.quantity("3")
        hp_pro.add_to_cart()
        main_page.back_to_main()
        main_page.cart()
        self.count = cart_pop_up.total_items_in_cart()
        self.assertTrue(self.count,"7 Item" )





