class Locators:
    def __init__(self, driver):
        self.driver = driver

    #General
    def general_cart(self):
        return self.driver.find_element_by_id('menuCart').click()

    #Main Page
    def mainpage_user(self):
        return self.driver.find_element_by_id("menuUserSVGPath").click()

    def mainpage_user_my_account(self):
        return self.driver.find_element_by_css_selector("label[translate=My_account]").click()

    def mainpage_user_my_orders(self):
        return self.driver.find_element_by_css_selector("label[translate=My_Orders]").click()

    def mainpage_user_sigh_out(self):
        return self.driver.find_element_by_css_selector("label[translate=Sign_out]").click()

    def mainpage_back_to_main(self):
        return self.driver.find_element_by_css_selector("div[class=logo]").click()

    def mainpage_speakers(self):
        return self.driver.find_element_by_id("speakersImg").click()

    def mainpage_tablets(self):
        return self.driver.find_element_by_id("tabletsImg").click()

    def mainpage_laptops(self):
        return self.driver.find_element_by_id("laptopsImg").click()

    def mainpage_mice(self):
        return self.driver.find_element_by_id("miceImg").click()

    def mainpage_headphones(self):
        return self.driver.find_element_by_id("headphonesImg").click()

    def mainpage_special_offer(self):
        return self.driver.find_element_by_id("see_offer_btn").click()

    def mainpage_chat_with_us(self):
        return self.driver.find_element_by_id("chatLogo").click()

    def mainpage_facebook(self):
        return self.driver.find_element_by_css_selector("img[name=follow_facebook]").click()

    def mainpage_twitter(self):
        return self.driver.find_element_by_css_selector("img[name=follow_twitter]").click()

    def mainpage_linkedin(self):
        return self.driver.find_element_by_css_selector("img[name=follow_linkedin]").click()

    #Tablets

    def tablets_home(self):
            return self.driver.find_element_by_link_text('HOME')

    def tablets_hp_elitepad(self):
        return self.driver.find_element_by_id("16").click()

    def tablets_hp_elite(self):
        return self.driver.find_element_by_id('17').click()

    def tablets_hp_pro(self):
        return self.driver.find_element_by_id('18').click()

    #HP ElitePad

    def elitepad_navigation_line(self):
        return self.driver.find_element_by_xpath("//div/nav/a[3]").text()

    def elitepad_tablets(self):
        return self.driver.find_element_by_link_text('TABLETS').click()

    def elitepad_price(self):
        return self.driver.find_element_by_xpath("//section/article/div/div[2]/h2").text()

    def elitepad_color_black(self):
        return self.driver.find_element_by_css_selector("span[title=BLACK]").click()

    def elitepad_color_gray(self):
        return self.driver.find_element_by_css_selector("span[title=GRAY]").click()

    def elitepad_quantity(self,text):
        self.driver.find_element_by_css_selector("input[name=quantity]").click()
        self.driver.find_element_by_css_selector("input[name=quantity]").send_keys(text)

    def elitepad_add_to_cart(self):
        self.driver.find_element_by_css_selector("button[name=save_to_cart]").click()

    #HP Elite

    def elite_navigation_line(self):
        return self.driver.find_element_by_xpath("//div/nav/a[3]").text()

    def elite_price(self):
        return self.driver.find_element_by_xpath("//section/article/div/div[2]/h2").text()

    def elite_color_black(self):
        return self.driver.find_element_by_css_selector("span[title=BLACK]").click()

    def elite_color_gray(self):
        return self.driver.find_element_by_css_selector("span[title=GRAY]").click()

    def elite_quantity(self,text):
        self.driver.find_element_by_css_selector("input[name=quantity]").click()
        self.driver.find_element_by_css_selector("input[name=quantity]").send_keys(text)

    def elite_add_to_cart(self):
        self.driver.find_element_by_css_selector("button[name=save_to_cart]").click()

    #HP Pro

    def pro_navigation_line(self):
        return self.driver.find_element_by_xpath("//div/nav/a[3]").text()

    def pro_price(self):
        return self.driver.find_element_by_xpath("//section/article/div/div[2]/h2").text()

    def pro_color_black(self):
        return self.driver.find_element_by_css_selector("span[title=BLACK]").click()

    def pro_color_gray(self):
        return self.driver.find_element_by_css_selector("span[title=GRAY]").click()

    def pro_quantity(self,text):
        self.driver.find_element_by_css_selector("input[name=quantity]").click()
        self.driver.find_element_by_css_selector("input[name=quantity]").send_keys(text)

    def pro_add_to_cart(self):
        self.driver.find_element_by_css_selector("button[name=save_to_cart]").click()

    #Cart Pop-Up

    def user(self):
        return self.driver.find_element_by_id("menuUserSVGPath").click()

    def user_my_account(self):
        return self.driver.find_element_by_css_selector("label[translate=My_account]").click()

    def user_my_orders(self):
        return self.driver.find_element_by_css_selector("label[translate=My_Orders]").click()

    def user_sigh_out(self):
        return self.driver.find_element_by_css_selector("label[translate=Sign_out]").click()

    def cart(self):
        return self.driver.find_element_by_id("menuCart").click()

    def back_to_main(self):
        return self.driver.find_element_by_css_selector("div[class=logo]").click()

    def cart_hovering(self):
        element_to_hover_over = self.driver.find_element_by_id("menuCart")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        return hover.perform()

    def total_for_payment(self):
        return self.driver.find_element_by_xpath("//*[@id=toolTipCart]/div/table/tfoot/tr[1]/td[2]/span").text

    def name_of_the_item(self, number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/h3").text

    def color_of_the_item(self, number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/label/span").text

    def qty_per_item(self, number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[2]/a/label").text

    def price_per_item(self, number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[3]/p").text

    def remove_item_from_cart(self, number_of_item_in_table):
        return self.driver.find_element_by_xpath(f"//table/tbody/tr[{number_of_item_in_table}]/td[3]/div").click()

    def total_items_in_cart(self):
        text = self.driver.find_element_by_xpath(
            '/html/body/header/nav/ul/li[2]/ul/li/tool-tip-cart/div/table/tfoot/tr[1]/td[1]/span/label').text
        return text

    def checkout(self):
        return self.driver.find_element_by_id("checkOutPopUp").click()

    #Cart

    def cart_navigation_line(self):
        return self.driver.find_element_by_xpath("//div/section/article/nav/a[2]").text()

    def cart_total_items_in_cart(self):
        return self.driver.find_element_by_css_selector("//div/section/article/h3/span").text()

    def cart_total_for_payment(self):
        return self.driver.find_element_by_xpath("//div[@id='shoppingCart']/table/tfoot/tr/td/span[2]").text()

    def cart_name_of_the_item(self, index):
        xpath = f'/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[2]/label'
        return self.driver.find_element_by_xpath(xpath).text()

    def cart_color_of_the_item(self, index):
        xpath = f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[4]"
        return self.driver.find_element_by_xpath(xpath).text()

    def cart_qty_per_item(self, index):
        xpath = f"/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[5]/label[2]"
        return self.driver.find_element_by_xpath(xpath).text

    def cart_price_per_item(self, index):
        xpath = f"//div[@id='shoppingCart']/table/tbody/tr[{index}]/td[6]/p"
        return self.driver.find_element_by_xpath(xpath).text()

    def cart_remove_item_from_cart(self, index):
        xpath = f"/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[6]/span/a[3]"
        return self.driver.find_element_by_xpath(xpath).click()

    def cart_edit_cart(self, index):
        xpath = f"/html/body/div[3]/section/article/div[1]/table/tbody/tr[{index}]/td[6]/span/a[1]"
        return self.driver.find_element_by_xpath(xpath).click()

    def cart_checkout(self):
        return self.driver.find_element_by_id("checkOutButton").click()

    #Checkout

    def checkout_navigation_line(self):
        return self.driver.find_element_by_css_selector("a[translate = ORDER_PAYMENT]").text()

    def checkout_edit_shipping_details(self):
        return self.driver.find_element_by_css_selector("a[translate = Edit_shipping_Details]").click

    def checkout_next_page(self):
        return self.driver.find_element_by_css_selector("button[id=next_btn]").click

    def checkout_payment_method_safepay(self):
        return self.driver.find_element_by_css_selector("img[alt=Safepay]").click

    def checkout_safepay_username(self, text):
        self.driver.find_element_by_css_selector("input[name=safepay_username]").click
        self.driver.find_element_by_css_selector("input[name=safepay_username]").send_keys(text)

    def checkout_safepay_password(self, text):
        self.driver.find_element_by_css_selector("input[name=safepay_password]").click
        self.driver.find_element_by_css_selector("input[name=safepay_password]").send_keys(text)

    def checkout_pay_now(self, text):
        return self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

    def checkout_order_succeed(self):
        return self.driver.find_element_by_css_selector("span[translate=Thank_you_for_buying_with_Advantage]").text()

    def checkout_checkout(self):
        return self.driver.find_element_by_id("checkOutPopUp").click()

    #My Orders

    def myorders_navigation_line(self):
        return self.driver.find_element_by_css_selector("a[translate = MY_ORDERS]").text()


    def myorders_order_number(self):
        return self.driver.find_element_by_xpath("//div[@id=myAccountContainer]/div/div/div[2]/div[1]/div[1]/label").text()

    def myorders_order_date(self):
        return self.driver.find_element_by_xpath("//div[@id=myAccountContainer]/div/div/div[2]/div[1]/div[2]/label").text()

    def myorders_total_price(self):
        return self.driver.find_element_by_xpath("//div[@id=myAccountContainer]/div/div/div[2]/div[1]/div[3]/label").text()





