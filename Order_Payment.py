from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Order_Payment:
    def __init__(self,driver):
        self.driver = driver

    def navigation_line(self):
        return self.driver.find_element_by_css_selector("a[translate=ORDER_PAYMENT]").text

    def wait_order(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[translate=ORDER_PAYMENT]")))

    def order_summary_total_payment(self):
        return self.driver.find_element_by_xpath("//div[@class='penetrationInCart']/label[2]/span").text

    def order_summary_total_items(self):
        return self.driver.find_element_by_xpath("//div[@id='userCart']/span").text

    def name_of_the_item(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='orderPayment']/div/tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/h3").text

    def color_of_the_item(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='orderPayment']/div/tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/label[2]").text

    def qty_per_item(self, index):
        return self.driver.find_element_by_xpath(f"//section/article/div/div[2]/tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/label[1]").text

    def price_per_item(self,index):
        return self.driver.find_element_by_xpath(f"//div[@id='orderPayment']/div/tool-tip-cart/div/table/tbody/tr[{index}]/td[3]/p").text

    def shipping_cost(self):
        return self.driver.find_element_by_css_selector("span[id=shippingCost]").text


