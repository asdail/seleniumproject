
class hp_ElitePad:
    def __init__(self,driver):
        self.driver = driver

#Check that you are in the right place = order payment
    def navigation_line(self):
        return self.driver.find_element_by_xpath("//div/nav/a[3]").text

    def hp_elitepad_wait(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span[title=BLUE]")))

    def cart(self):
        return self.driver.find_element_by_id('menuCart')

    def tablets(self):
        #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[id='tabletsImg']")))
        return self.driver.find_element_by_link_text('TABLETS').click()

    def price(self):
        return self.driver.find_element_by_xpath("//section/article/div/div[2]/h2").text

    def color_blue(self):
        return self.driver.find_element_by_css_selector("span[title=BLUE]").click()

    def color_gray(self):
        return self.driver.find_element_by_css_selector("span[title=GRAY]").click()

    def quantity(self,text):
        self.driver.find_element_by_css_selector("input[name=quantity]").click()
        self.driver.find_element_by_css_selector("input[name=quantity]").send_keys(text)

    def add_to_cart(self):
        self.driver.find_element_by_css_selector("button[name=save_to_cart]").click()
