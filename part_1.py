import unittest
from Tablets import *
from main_page import *
from HP_PRO import *
from Cart_pop_up import *
from Cart import *
from HP_ElitePad import *
from HP_ELITE_X2 import *

class AOSProject(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")

        self.driver.implicitly_wait(10)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()

        self.Main_page = Main_page(self.driver)
        self.Cart = Cart(self.driver)
        self.Tablets = Tablets(self.driver)
        self.HP_ElitePad = hp_ElitePad(self.driver)
        self.Cart_pop_up = Cart_pop_up(self.driver)
        self.HP_pro = HP_pro(self.driver)
        self.HP_elite_x2 = HP_elite_x2(self.driver)

        print('setUp')

    def tearDown(self):
        self.driver.close()

        print('tearDown')

    def exercise_1(self):
        self.Main_page.tablets()
        self.Tablets.hp_eletepad()
        self.HP_ElitePad.color_black()
        self.HP_ElitePad.quantity("2")
        self.HP_pro.add_to_cart()
        self.Main_page.back_to_main()

        self.Main_page.tablets()
        self.Tablets.hp_pro()
        self.HP_pro.color_gray()
        self.HP_pro.quantity("3")
        self.HP_pro.add_to_cart()
        self.Main_page.back_to_main()
        self.Main_page.cart()
        count = self.Cart_pop_up.total_items_in_cart()
        if self.assertTrue(count,"7 Item" ) == True:
            print("exercise_1 pass")
        else:
            print("exercise_1 fail")

    def exercise_2(self):
        self.Main_page.tablets()
        self.Tablets.hp_eletepad()
        self.hp_ElitePad.color_black()
        self.hp_ElitePad.quantity("2")
        self.hp_ElitePad.add_to_cart()
        self.Main_page.back_to_main()

        self.Main_page.tablets()
        self.Tablets.hp_pro()
        self.HP_pro.color_gray()
        self.HP_pro.quantity("3")
        self.HP_pro.add_to_cart()
        self.Main_page.back_to_main()
        self.Main_page.cart()
        self.Main_page.back_to_main()

        self.Main_page.tablets()
        self.Tablets.hp_elite()
        self.hp_ElitePad.color_black()
        self.hp_ElitePad.quantity("1")
        self.hp_ElitePad.add_to_cart()






