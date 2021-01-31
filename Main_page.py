from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page:
    def __init__(self,driver):
        self.driver = driver
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > header >nav >div  >a")))

# Click user
    def user(self):
        return self.driver.find_element_by_id("menuUserSVGPath").click()

# Click user mt account
    def user_my_account(self):
        return self.driver.find_element_by_css_selector("label[translate=My_account]").click()

# Click user - my orders
    def user_my_orders(self):
        return self.driver.find_element_by_css_selector("label[translate=My_Orders]").click()

# Click sigh out
    def user_sigh_out(self):
        return self.driver.find_element_by_css_selector("label[translate=Sign_out]").click()

# Click cart
    def cart(self):
        return self.driver.find_element_by_id("menuCart").click()

# Click on the logo of the web for back to main page
    def back_to_main(self):
        return self.driver.find_element_by_css_selector("div[class=logo]").click()

# Enter to speakers page
    def speakers(self):
        return self.driver.find_element_by_id("speakersImg").click()

# Enter to tablets page
    def tablets(self):
        return self.driver.find_element_by_id("tabletsImg").click()

# Enter to laptops  page
    def laptops(self):
        return self.driver.find_element_by_id("laptopsImg").click()

# Enter to mice page
    def mice(self):
        return self.driver.find_element_by_id("miceImg").click()

# Enter to headphones page
    def headphones(self):
        return self.driver.find_element_by_id("headphonesImg").click()

# Enter special offer
    def special_offer(self):
        return self.driver.find_element_by_id("see_offer_btn").click()

# Click chat with us
    def chat_with_us(self):
        return self.driver.find_element_by_id("chatLogo").click()

# Click move to facebook page
    def facebook(self):
        return self.driver.find_element_by_css_selector("img[name=follow_facebook]").click()

# Click move to twitter page
    def twitter(self):
        return self.driver.find_element_by_css_selector("img[name=follow_twitter]").click()

# Click move to linkedin page
    def linkedin(self):
        return self.driver.find_element_by_css_selector("img[name=follow_linkedin]").click()


