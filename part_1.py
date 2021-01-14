import unittest
from Cart_pop_up import *
from CheckOut import *
from HP_ELITE_X2 import *
from HP_PRO import *
from main_page import *

class AOSProject(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")

        self.driver.implicitly_wait(10)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()

    def add_two_products(self):
        Main_page.tablets()

