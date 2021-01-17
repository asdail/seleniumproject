from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self,driver):
        self.driver = driver

    def navigation_line(self):
        return self.driver.find_element_by_xpath("//div/section/article/nav/a[2]").text

    def wait_cart(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div/section/article/nav/a[2]")))

    def total_items_in_cart(self):
        return self.driver.find_element_by_xpath("//div/section/article/h3/span").text

    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//div[@id='shoppingCart']/table/tfoot/tr/td/span[2]").text

    def name_of_the_item(self,index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[2]/label").text

    def color_of_the_item(self, index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[4]/span").text

    def qty_per_item(self, index):
        return self.driver.find_element_by_xpath(f'//html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[5]').text

    def price_per_item(self,index):
        return self.driver.find_element_by_xpath(f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[6]/p").text

    def remove_item_from_cart(self,index):
        return self.driver.find_element_by_xpath(f'/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[6]/span/a[3]').click()

    def edit_cart(self, index):
        return self.driver.find_element_by_xpath(f'/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[6]/span/a[1]').click()

    def checkout(self):
        return self.driver.find_element_by_id("checkOutButton").click()


