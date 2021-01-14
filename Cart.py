
class Cart:
    def __init__(self,driver):
        self.driver = driver

    def navigation_line(self):
        return self.driver.find_element_by_xpath("//div/section/article/nav/a[2]").text()

    def total_items_in_cart(self):
        return self.driver.find_element_by_css_selector("//div/section/article/h3/span").text()

    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//div[@id='shoppingCart']/table/tfoot/tr/td/span[2]").text()

    def name_of_the_item(self):
        return self.driver.find_element_by_xpath("//div[@id='shoppingCart']/table/tbody/tr/td[2]").text()

    def color_of_the_item(self):
        return self.driver.find_element_by_xpath("//div[@id='shoppingCart']/table/tbody/tr/td[4]").text()

    def qty_per_item(self, index):
        return self.driver.find_element_by_xpath(f'/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[5]/label[2]').text()

    def price_per_item(self):
        return self.driver.find_element_by_xpath("//div[@id='shoppingCart']/table/tbody/tr/td[6]/p").text()

    def remove_item_from_cart(self):
        return self.driver.find_element_by_css_selector("a[translate=REMOVE]").click()

    def edit_cart(self, index):
        return self.driver.find_element_by_xpath(f'/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[6]/span/a[1]').click()

    def checkout(self):
        return self.driver.find_element_by_id("checkOutButton").click()


