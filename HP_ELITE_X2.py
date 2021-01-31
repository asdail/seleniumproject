
class HP_elite_x2:
    def __init__(self,driver):
        self.driver = driver

#Check that you are in the right place = order payment
    def navigation_line(self):
        return self.driver.find_element_by_xpath("//div/nav/a[3]").text()

# Display the price of the product
    def price(self):
        return self.driver.find_element_by_xpath("//section/article/div/div[2]/h2").text()

# Choose color for product -black
    def color_black(self):
        return self.driver.find_element_by_css_selector("span[title=BLACK]").click()

# Choose color for product -gray
    def color_gray(self):
        return self.driver.find_element_by_css_selector("span[title=GRAY]").click()

# Choose quantity - input
    def quantity(self,text):
        self.driver.find_element_by_css_selector("input[name=quantity]").click()
        self.driver.find_element_by_css_selector("input[name=quantity]").send_keys(text)

# Click add to cart
    def add_to_cart(self):
        self.driver.find_element_by_css_selector("button[name=save_to_cart]").click()


