import unittest
from Tablets import *
from main_page import *
from HP_PRO import *
from All_pages import *
from Cart import *
from HP_ElitePad import *
from HP_ELITE_X2 import *
from Order_Payment import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AOSProject(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")
        self.body = self.driver.find_element_by_xpath("/html/body")
        self.wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

        self.driver.implicitly_wait(15)

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
        self.order_payment = Order_Payment(self.driver)

        print('setUp')

    def tearDown(self):
        self.driver.close()

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
        self.tablets.wait_tablets()
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_elitepad.add_to_cart()
        self.main_page.back_to_main()
# Add the HP_pro tablet
        self.main_page.tablets()
        self.tablets.wait_tablets()
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()
        self.main_page.cart()
        self.main_page.back_to_main()
# Add the HP_elite_x2 tablet
        self.main_page.tablets()
        self.tablets.wait_tablets()
        self.tablets.hp_elite()
        self.hp_elite_x2.color_black()
        self.hp_elite_x2.quantity("1")
        self.hp_elite_x2.add_to_cart()



# Check the III item (HP_elite_x2 tablet)
        self.all_pages.cart_hovering()
        self.assertIn("HP ELITE X2", self.all_pages.name_of_the_item("1"))
        self.assertIn("BLACK",self.all_pages.color_of_the_item("1"))
        self.assertIn("1",self.all_pages.qty_per_item("1"))
        self.assertIn("$1,279",self.all_pages.price_per_item("1"))

# Check the II item (HP_pro tablet)
        self.all_pages.cart_hovering()
        self.assertIn("HP PRO", self.all_pages.name_of_the_item("2"))
        self.assertIn("GRAY",self.all_pages.color_of_the_item("2"))
        self.assertIn("3",self.all_pages.qty_per_item("2"))
        self.assertIn("$1,437",self.all_pages.price_per_item("2"))

# Check the I item (HP_ElitePad tablet)
        self.all_pages.cart_hovering()
        self.assertIn("HP ELITEPAD 1000 G2",self.all_pages.name_of_the_item("3"))
        self.assertIn("BLUE",self.all_pages.color_of_the_item("3"))
        self.assertIn("2",self.all_pages.qty_per_item("3"))
        self.assertIn("$2,018",self.all_pages.price_per_item("3"))



    def test_exercise_3(self):
        # Add the new product for the cart
        self.main_page.tablets()
        self.tablets.wait_tablets()
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        # Add another product for the cart
        self.main_page.tablets()
        self.tablets.wait_tablets()
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
        self.tablets.wait_tablets()
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        # Add another product for the cart
        self.main_page.tablets()
        self.tablets.wait_tablets()
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        # Go to Cart
        self.all_pages.cart()

        # Check If I'm in the right place
        navigation_line = self.cart.navigation_line()
        self.assertEqual("SHOPPING CART",navigation_line)


    def test_exercise_5(self):
# Add the HP_ElitePad tablet (I product)
        self.main_page.tablets()
        self.tablets.wait_tablets()
        self.tablets.hp_elitepad()
        self.hp_elitepad.color_blue()
        self.hp_elitepad.quantity("2")
        self.hp_elitepad.add_to_cart()
        self.main_page.back_to_main()

# Add the HP_pro tablet (II product)
        self.main_page.tablets()
        self.tablets.wait_tablets()
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()
        self.main_page.cart()
        self.main_page.back_to_main()

# Add the HP_elite_x2 tablet (III product)
        self.main_page.tablets()
        self.tablets.wait_tablets()
        self.tablets.hp_elite()
        self.hp_elite_x2.color_black()
        self.hp_elite_x2.quantity("1")
        self.hp_elite_x2.add_to_cart()
        self.main_page.back_to_main()

# Go to cart and check for details
        self.main_page.cart()

# Create variables for the I item (HP  Elite X2 tablet) - in cart
        cart_hp_elite_x2_name = self.cart.name_of_the_item("1")
        cart_hp_elite_x2_color = self.cart.color_of_the_item("1")
        cart_hp_elite_x2_qty = self.cart.qty_per_item("1")
        cart_hp_elite_x2_price = self.cart.price_per_item("1")

# Create variables for the II item (HP Pro tablet) - in cart
        cart_hp_pro_name = self.cart.name_of_the_item("2")
        cart_hp_pro_color = self.cart.color_of_the_item("2")
        cart_hp_pro_qty = self.cart.qty_per_item("2")
        cart_hp_pro_price = self.cart.price_per_item("2")

#  Create variables for the III item (HP ElitePad tablet) - in cart
        cart_hp_elite_pad_name = self.cart.name_of_the_item("3")
        cart_hp_elite_pad_color = self.cart.color_of_the_item("3")
        cart_hp_elite_pad_qty = self.cart.qty_per_item("3")
        cart_hp_elite_pad_price = self.cart.price_per_item("3")

# Total product and total for pay in the cart - new variables
        cart_total_payment = self.cart.total_for_payment()
        cart_total_products = self.cart.total_items_in_cart()

#Go to checkout and create variables for the order summary
        self.cart.checkout()

# Create variables for the I item (HP  Elite X2 tablet) - in order summary
        summary_elite_x2_name = self.order_payment.name_of_the_item("1")
        summary_elite_x2_color = self.order_payment.color_of_the_item("1")
        summary_elite_x2_qty = self.order_payment.qty_per_item("1")
        summary_elite_x2_price = self.order_payment.price_per_item("1")

# Create variables for the II item (HP Pro tablet) - in order summary
        summary_pro_name = self.order_payment.name_of_the_item("2")
        summary_pro_color = self.order_payment.color_of_the_item("2")
        summary_pro_qty = self.order_payment.qty_per_item("2")
        summary_pro_price = self.order_payment.price_per_item("2")

# Create variables for the II item (HP ElitePad tablet) on order summary
        summary_elite_pad_name = self.order_payment.name_of_the_item("3")
        summary_elite_pad_color = self.order_payment.color_of_the_item("3")
        summary_elite_pad_qty = self.order_payment.qty_per_item("3")
        summary_elite_pad_price = self.order_payment.price_per_item("3")

# Total product and total for payment in order summary - new variables
        summary_total_payment = self.order_payment.order_summary_total_payment()
        summary_total_products = self.order_payment.order_summary_total_items()

#Performs a comparison between products in the cart and the order summary
#Comparison of HP pro
        self.assertIn(summary_pro_name, cart_hp_pro_name)
        self.assertIn(cart_hp_pro_qty, summary_pro_qty)
        self.assertIn(summary_pro_price, cart_hp_pro_price)
        print(f"The I product in your shopping cart is {cart_hp_pro_name} the quantity of the product is {cart_hp_pro_qty} "
              f"and the total payment for the product is {cart_hp_pro_price}$")
        print("----------------------------------------------------")

#Comparison of HP ElitePad
        self.assertIn(summary_elite_pad_name, cart_hp_elite_pad_name)
        self.assertIn(cart_hp_elite_pad_qty, summary_elite_pad_qty)
        self.assertIn(summary_elite_pad_price, cart_hp_elite_pad_price)
        print(f"The I product in your shopping cart is {cart_hp_elite_pad_name} the quantity of the product is {cart_hp_elite_pad_qty} "
              f"and the total payment for the product is {cart_hp_elite_pad_price}$")

        print("----------------------------------------------------")
#Comparison of HP ElitePad
        self.assertIn(summary_elite_x2_name, cart_hp_elite_x2_name)
        self.assertIn(cart_hp_elite_x2_qty, summary_elite_x2_qty)
        self.assertIn(summary_elite_x2_price, cart_hp_elite_x2_price)
        print(f"The I product in your shopping cart is {cart_hp_elite_x2_name} the quantity of the product is {cart_hp_elite_x2_qty} "
              f"and the total payment for the product is {cart_hp_elite_x2_price}$")
        print("----------------------------------------------------")

# Performs a comparison between the total products and payment in the cart and the total in the order summary
        self.assertIn(cart_total_products[1], summary_total_products)
        self.assertIn(cart_total_payment, summary_total_payment)
        print(f"Total products in cart is {cart_hp_pro_price}, and Total for payment is {cart_total_payment}")
        print("----------------------------------------------------")
        print(f"Total products in order summary is {summary_total_products}, and total for payment is {summary_total_payment}")

