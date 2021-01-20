from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#class for order and payment page - specific for order summary
class Order_Payment:
    def __init__(self,driver):
        self.driver = driver

# Check that you are in the right place on the site = order payment
    def navigation_line(self):
        return self.driver.find_element_by_css_selector("a[translate=ORDER_PAYMENT]").text

# General wait for this page by general element in the page
    def wait_order(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[translate=ORDER_PAYMENT]")))

# Display total payment in the order summary
    def order_summary_total_payment(self):
        return self.driver.find_element_by_xpath("//div[@class='penetrationInCart']/label[2]/span").text

# Display total items in the order summary
    def order_summary_total_items(self):
        return self.driver.find_element_by_xpath("//div[@id='userCart']/span").text

# Display the name of item in the order summary by index
    def name_of_the_item(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='orderPayment']/div/tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/h3").text

# Display the color of item in the order summary by index
    def color_of_the_item(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='orderPayment']/div/tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/label[2]").text

# Display the qty of item in the order summary by index
    def qty_per_item(self, index):
        return self.driver.find_element_by_xpath(f"//section/article/div/div[2]/tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/label[1]").text

# Display the price of item in the order summary by index
    def price_per_item(self,index):
        return self.driver.find_element_by_xpath(f"//div[@id='orderPayment']/div/tool-tip-cart/div/table/tbody/tr[{index}]/td[3]/p").text

# Display the shipping cost
    def shipping_cost(self):
        return self.driver.find_element_by_css_selector("span[id=shippingCost]").text


