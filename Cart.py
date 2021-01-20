from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self,driver):
        self.driver = driver
# Show me my location on the site
    def navigation_line(self):
        return self.driver.find_element_by_xpath("//div/section/article/nav/a[2]").text

# General wait for cart page by general element in the page
    def wait_cart(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div/section/article/nav/a[2]")))

# Display total products I have in my cart
    def total_items_in_cart(self):
        return self.driver.find_element_by_xpath("//div/section/article/h3/span").text

# Display total for payment I have to pay
    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//div[@id='shoppingCart']/table/tfoot/tr/td/span[2]").text

# Display the name of the item in cart by index for instance if I want the I product index = 1
    def name_of_the_item(self,index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[2]/label").text

# Display the color of the item in cart by index for instance if I want the I product index = 1
    def color_of_the_item(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[4]/span").text

# Display the qty of the item in cart by index for instance if I want the I product index = 1
    def qty_per_item(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[5]/label[@class='ng-binding']").text

# Display the price of the item in cart by index for instance if I want the I product index = 1
    def price_per_item(self,index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[6]/p").text

# Remove 1 item from the cart by index for instance if I want the I product index = 1
    def remove_item_from_cart(self,index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[6]/span/a[3]").click()

# Edit 1 item from the cart by index for instance if I want the I product index = 1
    def edit_cart(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[6]/span/a[1]").click()

# Click on the checkout button
    def checkout(self):
        return self.driver.find_element_by_id("checkOutButton").click()


