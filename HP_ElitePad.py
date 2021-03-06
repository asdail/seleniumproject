from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Class for hp elite pad page
class hp_ElitePad:
    def __init__(self,driver):
        self.driver = driver

#Check that you are in the right place = order payment
    def navigation_line(self):
        return self.driver.find_element_by_xpath("//div/nav/a[3]").text

# General wait for this page by general element in the page
    def hp_elitepad_wait(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span[title=BLUE]")))

    def cart(self):
        return self.driver.find_element_by_id('menuCart')

# Click on tablets in the navigation line
    def tablets(self):
        #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[id='tabletsImg']")))
        return self.driver.find_element_by_link_text('TABLETS').click()

# Display the price of the product
    def price(self):
        return self.driver.find_element_by_xpath("//section/article/div/div[2]/h2").text

# click for choose color - blue
    def color_blue(self):
        return self.driver.find_element_by_css_selector("span[title=BLUE]").click()

# click for choose color - gray
    def color_gray(self):
        return self.driver.find_element_by_css_selector("span[title=GRAY]").click()

# Choose quantity - input
    def quantity(self,text):
        self.driver.find_element_by_css_selector("input[name=quantity]").click()
        self.driver.find_element_by_css_selector("input[name=quantity]").send_keys(text)

# Click add to cart
    def add_to_cart(self):
        self.driver.find_element_by_css_selector("button[name=save_to_cart]").click()
