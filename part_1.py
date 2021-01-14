import unittest
from Tablets import *
from main_page import *
from HP_PRO import *
from All_pages import *
from Cart import *
from HP_ElitePad import *
from HP_ELITE_X2 import *
from Locators import Locators


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

        print('setUp')

    def tearDown(self):
        self.driver.close()

        print('tearDown')

    def exercise_1(self):
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
        self.all_pages = All_pages(self.driver)
        self.hp_pro = HP_pro(self.driver)
        self.hp_elite_x2 = HP_elite_x2(self.driver)

        self.main_page.tablets()
        self.tablets.hp_eletepad()
        self.hp_elitepad.color_black()
        self.hp_elitepad.quantity("2")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()

        self.main_page.tablets()
        self.tablets.hp_pro()
        self.hp_pro.color_gray()
        self.hp_pro.quantity("3")
        self.hp_pro.add_to_cart()
        self.main_page.back_to_main()
        self.all_pages.cart_hovering()
        count = self.all_pages.total_items_in_cart()
        if self.assertTrue(count,"(5 Item)" ) == True:
            print("exercise_1 pass")
        else:
            print("exercise_1 fail")

    def exercise_2(self):
# Add the HP_ElitePad tablet
        self.main_page.tablets()
        self.tablets.hp_eletepad()
        self.hp_elitepad.color_black()
        self.hp_elitepad.quantity("2")
        self.hp_elitepad.add_to_cart()
        self.main_page.back_to_main()
# Add the HP_pro tablet
        self.main_page.tablets()
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



EE = AOSProject.exercise_2()

