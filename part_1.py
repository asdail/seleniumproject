import unittest
from Tablets import *
from main_page import *
from HP_PRO import *
from All_pages import *
from Cart import *
from HP_ElitePad import *
from HP_ELITE_X2 import *
from Locators import Locators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class AOSProject(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")
        self.body = self.driver.find_element_by_xpath("/html/body")
        self.wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

        self.driver.implicitly_wait(10)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()

        self.main_page = Main_page(self.driver)
        self.cart = Cart(self.driver)
        self.tablets = Tablets(self.driver)
        self.hp_elitepad = hp_ElitePad(self.driver)
        self.cart_pop_up = All_pages(self.driver)
        self.hp_pro = HP_pro(self.driver)
        self.hp_elite_x2 = HP_elite_x2(self.driver)
        self.all_pages =All_pages(self.driver)

        print('setUp')

    def tearDown(self):
        #self.driver.close()

        print('tearDown')

    def test_exercise_1(self):
# Add the new product for the cart
        self.main_page.tablets()
        self.all_pages.wait()
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

# Add another product for the cart
        self.main_page.tablets()
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        self.all_pages.cart_hovering()
        count = self.all_pages.total_items_in_cart()
        self.assertEqual(count,"(5 Items)" )    # Check if the number of the item in the cart equal to what I ordered


    def test_exercise_2(self):
# Add the HP_ElitePad tablet
        self.main_page.tablets()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[id='16']")))
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_elitepad.add_to_cart()
        self.main_page.back_to_main()
# Add the HP_pro tablet
        self.main_page.tablets()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img[id='17']")))
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()
        self.main_page.cart()
        self.main_page.back_to_main()
# Add the HP_elite_x2 tablet
        self.main_page.tablets()
        self.tablets.hp_elite()
        self.hp_elite_x2.color_black()
        self.hp_elite_x2.quantity("1")
        self.hp_elite_x2.add_to_cart()



# Check the III item (HP_elite_x2 tablet)
        self.all_pages.cart_hovering()
        self.assertIn("BLACK",self.all_pages.color_of_the_item("1"))
        self.assertIn("1",self.all_pages.qty_per_item("1"))
        self.assertIn("$1,279",self.all_pages.price_per_item("1"))

# Check the II item (HP_pro tablet)
        self.all_pages.cart_hovering()
        self.assertIn("GRAY",self.all_pages.color_of_the_item("2"))
        self.assertIn("3",self.all_pages.qty_per_item("2"))
        self.assertIn("$1,437",self.all_pages.price_per_item("2"))

# Check the I item (HP_ElitePad tablet)
        self.all_pages.cart_hovering()
        self.assertIn("BLUE",self.all_pages.color_of_the_item("3"))
        self.assertIn("2",self.all_pages.qty_per_item("3"))
        self.assertIn("$2,018",self.all_pages.price_per_item("3"))



    def test_exercise_3(self):
        # Add the new product for the cart
        self.main_page.tablets()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img[id='16']")))
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        # Add another product for the cart
        self.main_page.tablets()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img[id='17']")))
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        # Remove I item from the cart
        self.all_pages.cart_hovering()
        self.all_pages.remove_item_from_cart(2)   # Remove the I item = Elite Pad

        # Check if the product is really removed
        remove = self.all_pages.total_items_in_cart()
        self.assertTrue(remove,"(3 Item)")


    def test_exercise_4(self):
        # Add the new product for the cart
        self.main_page.tablets()
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        # Add another product for the cart
        self.main_page.tablets()
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        # Go to Cart
        self.all_pages.cart()

        # Check If I'm in the right place
        navigation_line = self.cart.navigation_line()
        self.assertIn("Shopping Cart",navigation_line)


    def test_exercise_5(self):
# Add the HP_ElitePad tablet (I product)
        self.main_page.tablets()
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_elitepad.add_to_cart()
        self.main_page.back_to_main()

# Add the HP_pro tablet (II product)
        self.main_page.tablets()
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()
        self.main_page.cart()
        self.main_page.back_to_main()

# Add the HP_elite_x2 tablet (III product)
        self.main_page.tablets()
        self.tablets.hp_elite()
        self.hp_elite_x2.color_black()
        self.hp_elite_x2.quantity("1")
        self.hp_elite_x2.add_to_cart()